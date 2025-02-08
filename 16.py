import pandas as pd
import matplotlib.pyplot as plt

file_path = r"C:\Users\Sreenath Reddy\Downloads\country_wise_latest_modified.csv"
df = pd.read_csv(file_path)

new_cases_by_region = df.groupby('WHO Region')['New cases'].sum()

plt.figure(figsize=(12, 8))
new_cases_by_region.plot(kind='bar', color='skyblue')
plt.title('Number of New Cases Across Different WHO Regions')
plt.xlabel('WHO Region')
plt.ylabel('Number of New Cases')
plt.grid(axis='y')
plt.show()

plt.figure(figsize=(12, 8))
new_cases_by_region.plot(kind='pie', autopct='%1.1f%%', startangle=140, colormap='tab20')
plt.title('Distribution of New Cases Across Different WHO Regions')
plt.ylabel('') 
plt.show()
