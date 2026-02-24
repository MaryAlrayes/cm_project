import pandas as pd


# 2. Save it as a clean CSV for later use
data=pd.read_csv('dataset\diabetes_cleaned.csv')

# 3. Quick check: see the first 5 rows
print(data.head())

total_null = data.isnull().sum().sum()
print(f"There are {total_null} missing values")

print(data.shape)