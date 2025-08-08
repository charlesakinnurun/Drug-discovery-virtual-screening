import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/drug_cleaned.csv")

# How many compounds have a "rotatable_bonds" count greater than 5
count_rotatable_bonds_gt5 = df[df["rotatable_bonds"] > 5].shape[0]
print(f"Number of compounds with rotatable_bonds > 5: {count_rotatable_bonds_gt5}")