# Part 1: Data Loading and Basic Exploration

import pandas as pd

# Step 1: Load the metadata.csv file
df = pd.read_csv('metadata.csv')

# Step 2: Examine the first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Step 3: Check the DataFrame dimensions (rows, columns)
print("\nDataFrame shape (rows, columns):", df.shape)

# Step 4: Identify data types of each column
print("\nData types of each column:")
print(df.dtypes)

# Step 5: Check for missing values in each column
print("\nMissing values per column:")
print(df.isnull().sum())

# Step 6: Generate basic statistics for numerical columns
print("\nStatistical summary for numerical columns:")
print(df.describe())
