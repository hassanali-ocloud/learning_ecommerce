import pandas as pd

dates = pd.date_range("2023-01-01", periods=7, freq="D")
data = [100, 110, 115, 120, 125, 130, 140]

df = pd.DataFrame({"Date": dates, "Value": data})
df.set_index("Date", inplace=True)

# print(df)

# Downsample to 3-day averages
# print(df.resample("3D").mean())

# Upsample to hourly, forward-fill values
# print(df.resample("h").ffill().head(10))

# df["Rolling_Mean"] = df["Value"].rolling(window=3).mean()
# print(df)

# # Shift forward by 1 day
# df["Shifted"] = df["Value"].shift(1)
# print(df)

# # # Calculate daily change
# df["Daily_Change"] = df["Value"] - df["Shifted"]
# print(df)

# Reindex to introduce missing dates
# all_days = pd.date_range("2023-01-01", "2023-01-10", freq="D")
# print(all_days)
# df = df.reindex(all_days)
# print(df)

# # Fill missing values
# df["Value"] = df["Value"].interpolate()   # linear interpolation
# print(df)
