import pandas as pd

cricketers_data = {
    'Index': [1, 2, 3, 4, 5],
    'Name': ['David Warner', 'Kane Williamson', 'Steve Smith','Virat Kohli', 'Babar Azam'],
    'ICC Ranking': [1, 2, 3, 9, 4],
    'Highest Score': [335, 242, 239, 254, 196]
}

df = pd.DataFrame(cricketers_data)
df.index+=1
df.to_csv('cricketers.csv', index=False)
df_read = pd.read_csv('cricketers.csv')
print(df_read.head())
