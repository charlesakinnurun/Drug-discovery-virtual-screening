import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/drug_cleaned.csv")

# For each unique "protein_id", what is the average "binding_affinity"
avg_affinity_by_protein = df.groupby("protein_id")["binding_affinity"].mean()
print("Average binding_affinity for each unique protein_id")
print(avg_affinity_by_protein)