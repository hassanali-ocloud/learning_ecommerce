import pandas as pd
import numpy as np

def fill_missing(df: pd.DataFrame) -> pd.DataFrame:
    df["age"] = df["age"].apply(lambda x: 0 if pd.isna(x) else x)
    print(df)
    return df

def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
  columns = ["student_id","age"]
  df = pd.DataFrame(student_data , columns = columns)
  print(df)
  fill_missing(df)

data = [
  [1, 15],
  [2, None],
  [3, 11],
  [4, 20]
]

createDataframe(data)