import pandas as pd

def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
    # Optimized
    # columns = ["student_id","age"]
    # df = pd.DataFrame(student_data , columns = columns)
    df = pd.DataFrame(student_data)
    df.columns = ["student_id", "name"]
    print(df)

data = [
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]

createDataframe(data)