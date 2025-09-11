import sqlite3
import os

class SqLite:
    def __init__(self, database_name):
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()

    def create_table(self, table_name, columns: list):
        columns_def = ", ".join([f"{col[0]} {col[1]} {col[2]}" for col in columns])
        full_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_def})"
        self.cursor.execute(full_query)
        self.connection.commit()
    
    def insert_into_table(self, table_name, datas: list):
        data_def = ", ".join([f"(\"{data[0]}\", \"{data[1]}\", \"{data[2]}\")" for data in datas])
        full_query = f"INSERT INTO {table_name} VALUES {data_def}"
        self.cursor.execute(full_query)
        self.connection.commit()

    def load_data(self, table_name, id):
        full_query = f"SELECT * FROM {table_name} WHERE id = {id}"
        self.cursor.execute(full_query)
        result = self.cursor.fetchone()
        return result
    
    def close_db(self):
        self.connection.close()

database_name = "animalDb.db"

if os.path.exists(database_name):
    os.remove(database_name)

sqLiteObj = SqLite(database_name)
sqLiteObj.create_table("animals", [["id", "INTEGER", "PRIMARY KEY"], ["name", "TEXT", ""], ["category", "TEXT", ""]])
sqLiteObj.insert_into_table("animals", [["0", "tiger", "mammal"], ["1", "crocodile", "reptile"], ["2", "sparrow", "bird"]])
print(sqLiteObj.load_data("animals", 2))


# Create Table
# Insert Data
# Select Data
# Do with OOP