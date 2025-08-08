import pandas as pd

# Load the dataset
df = pd.read_csv("datasets/drug_cleaned.csv")

# What is the average "hydrophobicity" for compounds that are considered active ("active" = 1) versus those that are not ("active" = 0)?
avg_hydrophobicity_active = df[df["active"] == 1]["hydrophobicity"].mean()
avg_hydrophobicity_inactive = df[df["active"] == 0]["hydrophobicity"].mean()
print(f"Average hydrophobicity for active compounds: {avg_hydrophobicity_active}")
print(f"AVerage hydrophobicity for inactive compound: {avg_hydrophobicity_inactive}")