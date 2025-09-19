import pandas as pd
import numpy as np

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    out = weather.pivot(index="month", columns="city", values="temperature")
    print(out)
    return out

def createDataframe(city_data: list[list]) -> pd.DataFrame:
    columns = ["city", "month", "temperature"]
    df = pd.DataFrame(city_data, columns=columns)
    return df

data = [
    ["Jacksonville", "January", 13],
    ["Jacksonville", "February", 23],
    ["Jacksonville", "March", 38],
    ["Jacksonville", "April", 5],
    ["Jacksonville", "May", 34],
    ["ElPaso", "January", 20],
    ["ElPaso", "February", 6],
    ["ElPaso", "March", 26],
    ["ElPaso", "April", 2],
    ["ElPaso", "May", 43],
]

df = createDataframe(data)
# print(df)
pivotTable(df)