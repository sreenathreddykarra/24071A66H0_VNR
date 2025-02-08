import pandas as pd
import matplotlib.pyplot as plt

file_path = r"C:\Users\Sreenath Reddy\Downloads\country_wise_latest_modified.csv"
df = pd.read_csv(file_path)

plt.figure(figsize=(10, 6))
plt.scatter(df['Confirmed'], df['Deaths'], alpha=0.5, color='blue')
plt.title('Relationship between Confirmed Cases and Deaths')
plt.xlabel('Confirmed Cases')
plt.ylabel('Deaths')
plt.grid(True)
plt.show()
