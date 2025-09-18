import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("../data.csv")

# Boxplot: Salary distribution per city
sns.boxplot(x="City", y="Salary", data=df)
plt.title("Salary Distribution by City")
plt.show()

# Pairplot: relationship between all numeric columns
sns.pairplot(df)
plt.show()