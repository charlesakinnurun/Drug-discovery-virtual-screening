import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/drug_cleaned.csv")

# Find all compounds that have a `binding_affinity` greater than the overall 75th percentile and are also `active` (1).
affinity_75th_percentile = df["binding_affinity"].quantile(0.75)
high_affinity_active_compounds = df[(df["binding_affinity"] > affinity_75th_percentile) & (df["active"] == 1)]
num_high_affinity_active_compounds = len(high_affinity_active_compounds)

# Display the result
print(f"Number of active compounds with binding_affinity > 75th percentile: {num_high_affinity_active_compounds}")
print("First 5 of thees compounds")
print(high_affinity_active_compounds[["compound_id","binding_affinity","active"]])
