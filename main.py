import pandas as pd

df = pd.read_csv("Sales_data.csv")

# Explore
print(df.head())
print(df.info())
print(df.describe())

# Feature Engineering
df["Total_Sales"] = df["Quantity"] * df["Price"]

# Analysis
print("\nTotal Revenue:", df["Total_Sales"].sum())
print("Average Order Value:", df["Total_Sales"].mean())

print("\nBest Selling Product:")
print(df.loc[df["Total_Sales"].idxmax()])

print("\nCategory-wise Sales:")
print(df.groupby("Category")["Total_Sales"].sum())
