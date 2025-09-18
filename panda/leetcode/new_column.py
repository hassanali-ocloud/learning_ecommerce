import pandas as pd

def new_column(df: pd.DataFrame) -> pd.DataFrame:
  df["bonus"] = df["age"] * 2
  print(df)

def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
  columns = ["student_id","age"]
  df = pd.DataFrame(student_data , columns = columns)
  new_column(df)

data = [
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]

createDataframe(data)