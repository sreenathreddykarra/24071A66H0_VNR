import pandas as pd
import matplotlib.pyplot as plt

file_path = r"C:\Users\Sreenath Reddy\Downloads\country_wise_latest_modified.csv"
df = pd.read_csv(file_path)

plt.figure(figsize=(12, 8))
plt.plot(df['Country/Region'], df['Confirmed'], label='Confirmed Cases', marker='o')
plt.plot(df['Country/Region'], df['Confirmed last week'], label='Confirmed Cases Last Week', marker='x')
plt.title('Change in Confirmed Cases Compared to Last Week')
plt.xlabel('Country/Region')
plt.ylabel('Number of Cases')
plt.xticks(rotation=90)  
plt.legend()
plt.grid(True)
plt.tight_layout() 
plt.show()
