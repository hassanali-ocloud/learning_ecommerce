import pandas as pd

# From a Python list
data = [10, 20, 30, 40]
s = pd.Series(data)

print(s)


# From a dictionary of lists
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "London", "Paris"]
}

df = pd.DataFrame(data)
print(df)
