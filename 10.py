import pandas as pd

file_path = r"C:\Users\Sreenath Reddy\Downloads\country_wise_latest_modified.csv"
df = pd.read_csv(file_path)

print("Original DataFrame:")
print(df)

print("\nMissing Values:")
print(df.isnull().sum())

df_filled = df.fillna(0)

print("\nDataFrame with Missing Values Filled:")
print(df_filled)
