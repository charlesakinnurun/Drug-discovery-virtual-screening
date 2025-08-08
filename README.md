# Introduction
![Drug discovery](assets/drug.png)
***
The drug_discovery_virtual_screening.csv file contains data from a virtual screening experiment in the field of drug discovery. In these experiments, computational models are used to predict which chemical compounds are most likely to bind effectively to a specific biological target, such as a protein.
Each row in the dataset represents a single chemical compound (compound_id) and its interaction with a particular protein target (protein_id). The columns provide a mix of information about the compounds and their protein targets, including:
* Compound properties: Attributes like molecular_weight, logp (a measure of a compound's lipophilicity), h_bond_donors, h_bond_acceptors, and rotatable_bonds, which are all key indicators of a drug's potential.
* Protein properties: Features of the target protein, such as its protein_length and protein_pi (isoelectric point).
* Interaction metrics: The binding_affinity column, which is a crucial metric that quantifies the strength of the interaction between the compound and the protein.
* Outcome: The active column, a binary flag that indicates whether the compound was classified as active (1) or inactive (0) in the screening.
## Cleaning
Data cleaning is a critical step in any data analysis process. Based on a preliminary look at your drug_discovery_virtual_screening.csv file, here are the key steps you can take to clean the data.
1. Identify and Handle Missing Values
The initial inspection of your dataset revealed that the following columns have 60 missing values each:
* logp
* polar_surface_area
* hydrophobicity
Dealing with these missing values is the most important cleaning step for your dataset. There are a few common strategies you can use, and the best choice depends on your specific analysis goals.
* Imputation: You can replace the missing values with a calculated value, such as the mean, median, or mode of the respective column.
* Deletion: If the number of missing values is small (which it is here, representing only 3% of the total rows), you could choose to remove the rows containing these values.
2. Check for and Remove Duplicates
Although the initial summary does not show any obvious duplicates, it's good practice to check for them. Duplicate rows can skew your analysis, especially when calculating statistics or training models. You can easily identify and remove them using a function like df.drop_duplicates().
3. Verify Data Types
The data types for all columns appear to be correct. The compound_id and protein_id columns are correctly identified as object (string) types, while the numerical data, like molecular_weight and binding_affinity, are correctly identified as float64 or int64. This means you likely won't need to perform any data type conversions.
4. Address Outlier
It's always a good idea to examine the distributions of your numerical columns to check for outliers. An outlier is a data point that is significantly different from other observations. For example, a molecular_weight that is a thousand times larger than the rest could indicate a data entry error. Outliers can be handled by either removing the rows that contain them or transforming the data.
By following these steps, you can ensure your data is clean and reliable for further analysis or model building.
```python
import pandas as pd
import numpy as np

# Load the CSV file into a DataFrame
df = pd.read_csv("datasets/drug.csv")

# Step 1: Hanndle Missing Values
# Impute missing values with the median of each column
# The "logp", "polar_surface_area" and "hydrophobicity" were identified as having missing values
print(f"Number of rows before cleaning: {len(df)}")
df["logp"] = df["logp"].fillna(df["logp"].median())
df["polar_surface_area"] = df["polar_surface_area"].fillna(df["polar_surface_area"].median())
df["hydrophobicity"] = df["hydrophobicity"].fillna(df["hydrophobicity"].median())

# Step 2: Remove Duplicates
# Check for and remove any duplicate rows
df_cleaned = df.drop_duplicates()
print(f"Number of rows after removing duplicates: {len(df_cleaned)}")


# Step 3: Verify Data Types and Final Check
# Display the information about the cleaned DataFrame to confirm there are no more missing values
print("Information of the cleaned DataFrame")
print(df_cleaned.info())

# Save the Cleaned Data
df_cleaned.to_csv("datasets/drug_cleaned.csv")
print("Saved Successfully")
```
## Analysis
Here are 10 analytical questions you can solve using the pandas library and your drug_discovery_virtual_screening.csv dataset:
1. What is the mean binding_affinity for compounds in the dataset?
2. How many unique protein_ids are present in the data?
3. What are the minimum, maximum, and average molecular_weight of all compounds?
4. Which compound_id has the highest binding_affinity, and what is its value?
5. What is the average hydrophobicity for compounds that are considered active (where active is 1) versus those that are not (active is 0)?
6. For each unique protein_id, what is the average binding_affinity?
7. How many compounds have a rotatable_bonds count greater than 5?
8. What is the correlation coefficient between molecular_weight and binding_affinity?
9. Find all compounds that have a binding_affinity greater than the overall 75th percentile and are also active (1).
10. Calculate the average protein_length and protein_pi for all compounds with h_bond_donors greater than or equal to 3 and h_bond_acceptors less than or equal to 5.
#### Calculate the average protein_length and protein_pi for all compounds with h_bond_donors greater than or equal to 3 and h_bond_acceptors less than or equal to 5.
```python
import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/drug_cleaned.csv")

# 10. Calculate the average `protein_length` and `protein_pi` for all compounds with `h_bond_donors` >= 3 and `h_bond_acceptors` <= 5.
filtered_compounds = df[(df['h_bond_donors'] >= 3) & (df['h_bond_acceptors'] <= 5)]
avg_protein_length = filtered_compounds['protein_length'].mean()
avg_protein_pi = filtered_compounds['protein_pi'].mean()
print(f"\n10. Average protein_length for specified conditions: {avg_protein_length}")
print(f"    Average protein_pi for specified conditions: {avg_protein_pi}")
```
#### What is the average hydrophobicity for compounds that are considered active (where active is 1) versus those that are not (active is 0)?
```python
import pandas as pd

# Load the dataset
df = pd.read_csv("datasets/drug_cleaned.csv")

# What is the average "hydrophobicity" for compounds that are considered active ("active" = 1) versus those that are not ("active" = 0)?
avg_hydrophobicity_active = df[df["active"] == 1]["hydrophobicity"].mean()
avg_hydrophobicity_inactive = df[df["active"] == 0]["hydrophobicity"].mean()
print(f"Average hydrophobicity for active compounds: {avg_hydrophobicity_active}")
print(f"AVerage hydrophobicity for inactive compound: {avg_hydrophobicity_inactive}")
```
#### Which compound_id has the highest binding_affinity, and what is its value?
```python
import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/drug_cleaned.csv")

# Which "compound_id" has the highest "binding_affinity", and what is its value
max_affinity_compound = df.loc[df["binding_affinity"].idxmax()]
print(f"Compound with the highest binding_affinity: {max_affinity_compound["compound_id"]}")
print(f"Highest binding_affinity value: {max_affinity_compound["binding_affinity"]}")
```
#### What is the mean binding_affinity for compounds in the dataset?
```python
import pandas as pd

# Load the data
df = pd.read_csv("datasets/drug_cleaned.csv")

# What is the mean "binding_affinity" for compounds in the dataset
mean_binding_affinity = df["binding_affinity"].mean()
print(f"Mean binding_affinity: {mean_binding_affinity}")
```
The remaining analysis can be found
[here](/script/)
## Tools I Used
* Python (pandas)
* Git
* Vscode
