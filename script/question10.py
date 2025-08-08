import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/drug_cleaned.csv")

# 10. Calculate the average `protein_length` and `protein_pi` for all compounds with `h_bond_donors` >= 3 and `h_bond_acceptors` <= 5.
filtered_compounds = df[(df['h_bond_donors'] >= 3) & (df['h_bond_acceptors'] <= 5)]
avg_protein_length = filtered_compounds['protein_length'].mean()
avg_protein_pi = filtered_compounds['protein_pi'].mean()
print(f"\n10. Average protein_length for specified conditions: {avg_protein_length}")
print(f"    Average protein_pi for specified conditions: {avg_protein_pi}")