import pandas as pd

file_path = r"C:\Users\Sreenath Reddy\Downloads\country_wise_latest_modified.csv"
df = pd.read_csv(file_path)

print("Original DataFrame:")
print(df)

df_dropped_column = df.drop(columns=['1 week % increase'])

print("DataFrame after Dropping '1 week % increase' Column:")
print(df_dropped_column)
