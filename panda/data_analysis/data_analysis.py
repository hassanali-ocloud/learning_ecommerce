import pandas as pd

df = pd.read_csv("../data.csv")

# print(df.describe())

# print("Mean Age:", df["Age"].mean())
# print("Max Salary:", df["Salary"].max())
# print("Median Salary:", df["Salary"].median())

# Introduce some missing values
# df.loc[2, "Salary"] = None
# print(df, "\n") 

# # Detect missing values
# print(df.isnull().sum())

# # Fill missing values
# df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
# print(df)

# # Drop rows with missing values
# df_clean = df.dropna()
# print(df_clean)

# print(df.groupby("City")["Salary"].agg(["mean", "max", "min"]))

# print(df[["Age", "Salary"]].corr())