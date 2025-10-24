import pandas as pd

# Sample data
data = {
    "Num": range(1, 11),  # 10 rows, 1–10
    "Value1": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
    "Value2": [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],
    "Value3": [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to Excel
df.to_excel("Table.xlsx", sheet_name="I", index=False)

print("Sample Table.xlsx created successfully!")
