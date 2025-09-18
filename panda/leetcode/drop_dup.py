import pandas as pd

def dropDuplicate(df: pd.DataFrame) -> pd.DataFrame:
  df = df.drop_duplicates(subset="age", keep="first")
  print(df)

def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
  columns = ["student_id","age"]
  df = pd.DataFrame(student_data , columns = columns)
  dropDuplicate(df)

data = [
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]

createDataframe(data)