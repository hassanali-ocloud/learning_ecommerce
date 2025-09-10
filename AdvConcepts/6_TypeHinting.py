from typeguard import typechecked
from pydantic import BaseModel

def customFunction(parameter: int):
    print(parameter)

def customFunc2(paras: list[int]):
    for para in paras:
        print(para)

customFunction("asf")
customFunc2([2,"3",4])