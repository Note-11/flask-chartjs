import pandas as pd
import random

# Generate sample data
num_rows = 20
data = {
    "Num": range(1, num_rows + 1),
    "TransactionID": [f"T{1000 + i}" for i in range(num_rows)],
    "Amount": [round(random.uniform(10, 1000), 2) for _ in range(num_rows)],
    "RiskScore": [random.randint(0, 100) for _ in range(num_rows)],
    "Flagged": [random.choice([0, 1]) for _ in range(num_rows)]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to Excel
df.to_excel("Table.xlsx", sheet_name="I", index=False)

print("Sample fraud Table.xlsx created successfully!")
