from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, ForeignKey, func

# engine = create_engine('sqlite:///mydatabase.db', echo=True)
engine = create_engine('postgresql+psycopg2://postgres:zxcv1234Z%40@localhost:5432/postgres', echo=True)
meta = MetaData()

people = Table(
    "people",
    meta,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('age', Integer)
)

things = Table(
    "things",
    meta,
    Column('id', Integer, primary_key=True),
    Column('description', String, nullable=False),
    Column('value', Float),
    Column('owner', Integer, ForeignKey('people.id'))
)

meta.create_all(engine)

conn = engine.connect()

insert_people = people.insert().values([
    {'name': 'Mike', 'age': 30},
    {'name': 'Bob', 'age': 20},
    {'name': 'Anna', 'age': 25},
    {'name': 'John', 'age': 35},
    {'name': 'Clara', 'age': 40},
])

insert_things = things.insert().values([
    {'owner': 2, 'description': 'Laptop', 'value': 800.50},
    {'owner': 2, 'description': 'Mouse', 'value': 50.50},
    {'owner': 2, 'description': 'Keyboard', 'value': 100.50},
    {'owner': 3, 'description': 'Book', 'value': 30},
    {'owner': 4, 'description': 'Bottle', 'value': 10.50},
    {'owner': 5, 'description': 'Speakers', 'value': 80.50},
])

# conn.execute(insert_people)
# conn.execute(insert_things)
# conn.commit()

# join_statement = people.join(things, people.c.id == things.c.owner)
# select_statement = people.select().with_only_columns(people.c.name, things.c.description).select_from(join_statement)

group_by_statement = things.select().with_only_columns(things.c.owner, func.sum(things.c.value)).group_by(
    things.c.owner).having(func.sum(things.c.value) > 50)

result = conn.execute(group_by_statement)
for x in result.fetchall():
    print(x)


# =================================================================
# select_Statement = people.select().where(people.c.age > 30)

# insert_statement = people.insert().values(name='Bob', age=40)
# result = conn.execute(insert_statement)

# update_statement = people.update().where(people.c.name == 'Bob').values(age = 10)

# delete_statement = people.delete().where(people.c.name == 'Mike')

# result = conn.execute(delete_statement)
# conn.commit()
# print(result.fetchall())

# conn.execute(text("Create table if not exists people(name str, age integer)"))
# conn.commit()

# from sqlalchemy.orm import Session

# session = Session(engine)
# session.execute(text("insert into people (name, age) values (\"Mike\", 30);"))