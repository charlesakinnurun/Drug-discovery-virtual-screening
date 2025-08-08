import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/drug_cleaned.csv")

# What are the minimum, maximum and average "molecular_weight" of all compounds
min_mw = df["molecular_weight"].min()
max_mw = df["molecular_weight"].max()
avg_mw = df["molecular_weight"].mean()

# Display the result
print(f"Minimum molecular_weight: {min_mw}")
print(f"Maximum molecular_weight: {max_mw}")
print(f"Average molecular_weight: {avg_mw}")