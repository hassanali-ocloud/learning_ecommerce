from sqlalchemy import create_engine, Integer, String, Float, Column, ForeignKey, func
import pandas as pd

engine = create_engine('postgresql+psycopg2://postgres:zxcv1234Z%40@localhost:5432/postgres', echo=False)

df = pd.read_sql("SELECT * FROM people", con=engine)

print(df)

# new_data = pd.DataFrame({'name': ['Florian', 'Jack'], 'age': [26, 90]})
# new_data.to_sql('people', con=engine, if_exists='append', index=False)