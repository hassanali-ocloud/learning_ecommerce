import pandas as pd

def rename(df: pd.DataFrame) -> pd.DataFrame:
    df["age"] = df["age"].astype(str)
    print(df)

def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
  columns = ["student_id","age"]
  df = pd.DataFrame(student_data , columns = columns)
  rename(df)

data = [
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]

createDataframe(data)