import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/drug_cleaned.csv")

# What is the correlation coefficient between "molecular_weight" and "binding_affinity"
correlation = df["molecular_weight"].corr(df["binding_affinity"])
print(f"Correlation between molecular_weight and binding_affinity: {correlation}")