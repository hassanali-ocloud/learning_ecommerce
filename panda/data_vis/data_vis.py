import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data.csv")

# Line plot of Age vs Salary
# df.plot(x="Age", y="Salary", kind="line", marker="o")
# plt.title("Age vs Salary")
# plt.show()

# df.groupby("City")["Salary"].mean().plot(kind="bar", color="skyblue")
# plt.title("Average Salary by City")
# plt.ylabel("Salary")
# plt.show()

# df["Age"].plot(kind="hist", bins=5, edgecolor="black")
# plt.title("Age Distribution")
# plt.show()

df.plot(kind="scatter", x="Age", y="Salary", color="red")
plt.title("Age vs Salary (Scatter)")
plt.show()