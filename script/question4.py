import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/drug_cleaned.csv")

# Which "compound_id" has the highest "binding_affinity", and what is its value
max_affinity_compound = df.loc[df["binding_affinity"].idxmax()]
print(f"Compound with the highest binding_affinity: {max_affinity_compound["compound_id"]}")
print(f"Highest binding_affinity value: {max_affinity_compound["binding_affinity"]}")