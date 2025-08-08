import pandas as pd

# Load the data
df = pd.read_csv("datasets/drug_cleaned.csv")

# What is the mean "binding_affinity" for compounds in the dataset
mean_binding_affinity = df["binding_affinity"].mean()
print(f"Mean binding_affinity: {mean_binding_affinity}")