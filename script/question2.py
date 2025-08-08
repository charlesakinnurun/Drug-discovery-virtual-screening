import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/drug_cleaned.csv")

# How many unique "protein_id"s are present in the data
unique_protein_ids = df["protein_id"].nunique()
print(f"Number of unique protein_ids: {unique_protein_ids}")