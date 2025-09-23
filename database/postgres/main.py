import psycopg2

conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="zxcv1234Z@", port=5432)
cur = conn.cursor()

# cur.execute(
#     """
#     --sql
#     CREATE TABLE IF NOT EXISTS person(
#             id INT PRIMARY KEY,
#             name VARCHAR(255),
#             age INT,
#             gender CHAR    
#         );"""
#     )

# cur.execute("""
#     --sql
#     INSERT INTO person (id, name, age, gender) VALUES
#     (1, 'Alice Johnson', 28, 'F'),
#     (2, 'Bob Smith', 35, 'M'),
#     (3, 'Charlie Brown', 22, 'M'),
#     (4, 'Diana Prince', 30, 'F'),
#     (5, 'Ethan Clark', 41, 'M'),
#     (6, 'Fiona Adams', 26, 'F');
# """)

# cur.execute("""--sql
#             SELECT * FROM person WHERE name ='Bob Smith';
# """)
# cur.execute("""--sql
#             select * from person where age > 20;
# """)

# for row in cur.fetchall():
#     print(row)

query = """SELECT * FROM person WHERE age > %s;"""
params = (20,)
formatted_query = cur.mogrify(query, params)
print(formatted_query)

cur.execute(formatted_query)
print(cur.fetchall())


conn.commit()

cur.close()
conn.close()