import pandas as pd
from pathlib import Path

data_path = Path("data")

dfs = []
for file in data_path.glob("*.csv"):
    df = pd.read_csv(file)
    dfs.append(df)

# Combine all CSVs
data = pd.concat(dfs, ignore_index=True)

# Normalize product name and filter Pink Morsel
data["product"] = data["product"].str.strip().str.lower()
data = data[data["product"] == "pink morsel"]

# 🔥 CREATE Sales column (this was missing)
data["Sales"] = data["quantity"] * data["price"]

# Select required columns
final_data = data[["Sales", "date", "region"]]

# Rename columns (safe way, no inplace)
final_data = final_data.rename(columns={
    "date": "Date",
    "region": "Region"
})

# Save output
final_data.to_csv("processed_sales.csv", index=False)

print("Processed File created Successfully!")
