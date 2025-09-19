import pandas as pd
import numpy as np

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    print(report)
    print("-------------")
    report = report.melt(id_vars=["city"], var_name="new_month", value_name="new_temp")
    print(report)
    return report

df = pd.DataFrame({
    "city": ["ElPaso", "Jacksonville"],
    "Jan": [20, 13],
    "Feb": [6, 23],
    "Mar": [26, 38]
})

meltTable(df)