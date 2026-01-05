import pandas as pd
from pathlib import Path

data_path = Path("data")

dfs = []
for file in data_path.glob("*.csv"):
    df = pd.read_csv(file)
    dfs.append(df)

# Combine all CSV files
data = pd.concat(dfs, ignore_index=True)

# Normalize product name
data["product"] = data["product"].str.strip().str.lower()

# Filter only Pink Morsel
data = data[data["product"] == "pink morsel"]

# 🔥 Clean price column if it has $ signs and convert to float
data["price"] = data["price"].replace({'\$': ''}, regex=True).astype(float)

# Create sales column
data["sales"] = data["quantity"] * data["price"]

# Sum sales by date and region
final_data = data.groupby(["date", "region"], as_index=False)["sales"].sum()

# Save output
final_data.to_csv("processed_sales.csv", index=False)

print("Processed file created successfully!")
