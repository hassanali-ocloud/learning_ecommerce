import pandas as pd

def modify(df: pd.DataFrame) -> pd.DataFrame:
  df["age"] = df["age"] * 2
  print(df)

def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
  columns = ["student_id","age"]
  df = pd.DataFrame(student_data , columns = columns)
  modify(df)

data = [
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]

createDataframe(data)