import pandas as pd

file_path = r"C:\Users\Sreenath Reddy\Downloads\country_wise_latest_modified.csv"
df = pd.read_csv(file_path)

print("Original DataFrame:")
print(df)

filtered_df = df[df['Confirmed'] > 10000]

print("\nFiltered DataFrame (Confirmed cases > 10,000):")
print(filtered_df)
