import pandas as pd

def dropMissing(df: pd.DataFrame) -> pd.DataFrame:
  df.dropna(subset="age", inplace=True, how='any')
  return df

def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
  columns = ["student_id","age"]
  df = pd.DataFrame(student_data , columns = columns)
  print(df)
  dropMissing(df)
  print(df)

data = [
  [1, 15],
  [2, 11],
  [3, ],
  [4, 20]
]

createDataframe(data)