from sqlalchemy import create_engine, Integer, String, Float, Column, ForeignKey, func
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

# engine = create_engine('sqlite:///mydatabase.db', echo=True)
engine = create_engine('postgresql+psycopg2://postgres:zxcv1234Z%40@localhost:5432/postgres', echo=False)

Base = declarative_base()

class Person(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)

    things = relationship('Thing', back_populates='person')

class Thing(Base):
    __tablename__ = 'things'
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    value = Column(Float)
    owner = Column(Integer, ForeignKey('people.id'))

    person = relationship('Person', back_populates='things')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# new_person = Person(name='King1', age=70)
# session.add(new_person)
# session.flush()

# new_thing = Thing(description='Mouse1', value=500, owner=new_person.id)
# session.add(new_thing)

# session.commit()

# print([t.description for t in new_person.things])
# print(new_thing.person.name)

# Query all persons with their things
# people = session.query(Person).all()
# result = session.query(Person.name, Person.age).all()
# result = session.query(Person).filter(Person.age > 40)
# result = session.query(Thing).filter(Thing.value <= 500).delete()
# result = session.query(Person).filter(Person.name == 'Charlie').update({'name': "Karla"})
# result = session.query(Person.name, Thing.description).join(Thing).all()
result = session.query(Thing.owner, func.sum(Thing.value)).group_by(Thing.owner).having(func.sum(Thing.value) > 50).all()
session.commit()
print(result)

session.close()