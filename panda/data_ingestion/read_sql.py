import sqlite3
import pandas as pd

# Connect to a SQLite database
conn = sqlite3.connect("my_database.db")

# Query the database
df = pd.read_sql("SELECT * FROM customers", conn)

print(df.head())
