import pandas as pd

def getDataframeSize(student_data: pd.DataFrame) -> list[int]:
    # return list[student_data.shape]
    return [len(student_data.columns), len(student_data)]

def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
    columns = ["student_id","age"]
    df = pd.DataFrame(student_data , columns = columns)
    print(getDataframeSize(df))

data = [
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]

createDataframe(data)