import pandas as pd

# Assuming df is already loaded from Part 1

# Step 1: Identify columns with many missing values
missing_counts = df.isnull().sum()
print("Missing values per column:")
print(missing_counts.sort_values(ascending=False))

# Step 2: Decide how to handle missing values
# For example, drop columns with more than 50% missing values
threshold = len(df) * 0.5
cols_to_drop = missing_counts[missing_counts > threshold].index
print("\nColumns to drop (more than 50% missing):", list(cols_to_drop))

df_cleaned = df.drop(columns=cols_to_drop)

# Step 3: For remaining missing values, fill with reasonable defaults or drop rows
# Example: Fill missing abstracts with empty string
if 'abstract' in df_cleaned.columns:
    df_cleaned['abstract'] = df_cleaned['abstract'].fillna('')

# Step 4: Convert date columns to datetime format
# Assume 'publish_time' is the publication date column
df_cleaned['publish_time'] = pd.to_datetime(df_cleaned['publish_time'], errors='coerce')

# Step 5: Extract year from publish_time for analysis
df_cleaned['year'] = df_cleaned['publish_time'].dt.year

# Step 6: Create new column: abstract word count
df_cleaned['abstract_word_count'] = df_cleaned['abstract'].apply(lambda x: len(str(x).split()))

# Quick check on cleaned data
print("\nCleaned DataFrame info:")
print(df_cleaned.info())

print("\nSample data after cleaning:")
print(df_cleaned.head())
