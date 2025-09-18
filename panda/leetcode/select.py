import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
  return students.loc[students["student_id"] == 2, ["age"]]

def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
    columns = ["student_id","age"]
    df = pd.DataFrame(student_data , columns = columns)
    # selectData(df)
    print(selectData(df))

data = [
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]

createDataframe(data)