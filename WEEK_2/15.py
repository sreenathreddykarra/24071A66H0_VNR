import pandas as pd
import matplotlib.pyplot as plt

file_path = r"C:\Users\Sreenath Reddy\Downloads\country_wise_latest_modified.csv"
df = pd.read_csv(file_path)

df['Active'] = df['Confirmed'] - df['Recovered'] - df['Deaths']

plt.figure(figsize=(12, 8))
df.boxplot(column='Active', by='Country/Region', vert=False)
plt.title('Variation of Active Cases Across Different Countries')
plt.suptitle('')  
plt.xlabel('Number of Active Cases')
plt.ylabel('Country/Region')
plt.grid(True)
plt.show()
