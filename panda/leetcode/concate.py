import pandas as pd
import numpy as np

def concate(df: pd.DataFrame, df_1: pd.DataFrame) -> pd.DataFrame:
    new = pd.concat([df, df_1])
    print(new)
    
def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
  columns = ["student_id","age"]
  df = pd.DataFrame(student_data , columns = columns)
  return df

data = [
  [1, 104],
  [2, 105],
  [3, 106],
  [4, 107]
]

data_1 = [
  [1, 100],
  [2, 101],
  [3, 102],
  [4, 103]
]

data = createDataframe(data)
data_1 = createDataframe(data)
concate(data, data_1)