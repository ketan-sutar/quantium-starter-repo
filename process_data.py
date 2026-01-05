import pandas as pd
from pathlib import Path

data_path = Path("data")

dfs = []
for file in data_path.glob("*.csv"):
    df = pd.read_csv(file)
    dfs.append(df)

data = pd.concat(dfs, ignore_index=True)

data["product"] = data["product"].str.strip().str.lower()
data = data[data["product"] == "pink morsel"]

data["Sales"] = data["quantity"] * data["price"]

final_data = data[["Sales", "date", "region"]]

final_data = final_data.rename(columns={
    "date": "Date",
    "region": "Region"
})

final_data.to_csv("processed_sales.csv", index=False)

print("Processed File created Successfully!")
