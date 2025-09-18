import pandas as pd

def read_xlsx():
    df = pd.read_excel("../data.xlsx", sheet_name="Sheet1")

    print(df.head())


def main():
    read_xlsx()

main()