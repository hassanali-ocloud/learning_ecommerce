import pandas as pd

def read_csv():
    df = pd.read_csv(
        "../data.csv",
        sep=",",
        usecols=["Name", "Age"]
    )

    print(df.head())


def main():
    read_csv()

main()