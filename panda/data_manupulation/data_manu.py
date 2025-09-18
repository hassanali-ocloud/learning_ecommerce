import pandas as pd

df = pd.read_csv("../data.csv")

#print(df["Name"])

# Select multiple columns (returns a DataFrame)
# print(df[["Name", "Salary"]])

# print(df.head(3))

# cities = df[df["City"].isin(["London", "Paris"])]
# print(cities)

# names_salaries = df[["Name", "Salary"]]
# new_names = names_salaries[names_salaries["Salary"] > 60000]
# print(new_names)

# df["Salary"] = df["Salary"] * 1.10

# df["Categorization"] = df["Salary"].apply(lambda x: "High Paying" if x < 60000 else "Low Paying")
# print(df)

# print(df["Salary"].mean())

# print(df.groupby("City")["Salary"].mean())

# print(df["Age"].value_counts())

# Sort by Age
# print(df.sort_values(by="Age"))

# Sort by Salary (descending)
# print(df.sort_values(by="Salary", ascending=False))
