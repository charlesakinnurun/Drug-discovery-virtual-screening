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