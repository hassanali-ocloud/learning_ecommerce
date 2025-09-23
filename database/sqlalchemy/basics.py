from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

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
meta.create_all(engine)

conn = engine.connect()

# select_Statement = people.select().where(people.c.age > 30)

# insert_statement = people.insert().values(name='Bob', age=40)
# result = conn.execute(insert_statement)

# update_statement = people.update().where(people.c.name == 'Bob').values(age = 10)

delete_statement = people.delete().where(people.c.name == 'Mike')

result = conn.execute(delete_statement)
conn.commit()
# print(result.fetchall())

# conn.execute(text("Create table if not exists people(name str, age integer)"))
# conn.commit()

# from sqlalchemy.orm import Session

# session = Session(engine)
# session.execute(text("insert into people (name, age) values (\"Mike\", 30);"))

# 23:34