import sys
sys.path.append("..")

from fastapi import Depends, HTTPException, status, APIRouter
from pydantic import BaseModel
from typing import Optional
from .. import models
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from ..database import SessionLocal, engine
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from datetime import datetime, timedelta
from jose import jwt, JWTError
from .auth import verify_password

SECRET_KEY = "e673746a75e70baa4e3aa2947a96cfb6404f0fe2dd73ce10b0c38b6a3ad670eb"
ALGORITHM = "HS256"

argon_context = CryptContext(schemes=["argon2"], deprecated="auto")

models.Base.metadata.create_all(bind=engine)

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="token")

class PasswordUpdate(BaseModel):
    old_password: str
    new_password: str

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={401: {"user": "Not Found"}}
)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

def get_password_hash(password):
    return argon_context.hash(password)

async def get_current_user(token: str = Depends(oauth2_bearer)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        user_id: int = payload.get("id")
        if username is None or user_id is None:
            raise get_user_exception()
        return {"username": username, "id": user_id}
    except JWTError as e:
        raise get_user_exception()

@router.get("/")
async def get_all_users(db: Session = Depends(get_db)):
    return db.query(models.Users).all()

@router.get("/{user_id}")
async def get_single_user_by_path(user_id: int, db: Session = Depends(get_db)):
    user_model =  db.query(models.Users).filter(models.Users.id == user_id).first()

    if user_model is not None:
        return user_model
    raise HTTPException(status_code=404, detail="User not found")

@router.get("/User/")
async def get_single_user_by_query(user_id: int, db: Session = Depends(get_db)):
    user_model =  db.query(models.Users).filter(models.Users.id == user_id).first()

    if user_model is not None:
        return user_model
    raise HTTPException(status_code=404, detail="User not found")

@router.put("/updatePassword")
async def update_password(
        password_update: PasswordUpdate,
        user: dict = Depends(get_current_user),
        db: Session = Depends(get_db)):

    user_model = db.query(models.Users).filter(models.Users.id == user.get("id")).first()
    if user_model is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    if not verify_password(password_update.old_password, user_model.hashed_password):
        raise HTTPException(status_code=404, detail="Wrong Password")

    user_model.hashed_password = get_password_hash(password_update.new_password)
    db.commit()
    db.refresh(user_model)
    return {"message": "Password changed successfully"}

@router.delete("/{user_id}")
async def delete_user(user_id: int,
                      user: dict = Depends(get_current_user),
                      db: Session = Depends(get_db)):
    if user is None:
        raise get_user_exception()

    db.query(models.Todos)\
        .filter(models.Todos.owner_id == user_id).delete()
    
    db.query(models.Users)\
        .filter(models.Users.id == user_id).delete()
    
    db.commit()
    return successfull_response(200)


def successfull_response(status_code: int):
    return {
        'status': status_code,
        'transaction': 'Successfull'
    }

# Exceptions
def get_user_exception():
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    return credentials_exception

def token_exception():
    token_exception_response = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return token_exception_response

