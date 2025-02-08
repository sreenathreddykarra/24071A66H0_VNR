import pandas as pd

df1 = pd.DataFrame({
    'ROLL NUMBER': ['24071A66G8','24071A66G9','24071A66H0','24071A66H1'],
    'Name': ['Pallavi', 'Praneeth', 'Sreenath', 'Nanditha']
})

df2 = pd.DataFrame({
   'ROLL NUMBER': ['24071A66H2','24071A66H3','24071A66H0','24071A66H1'],
    'Age': [18, 19, 18, 17]
})

merged_df = pd.merge(df1, df2, on='ROLL NUMBER', how='inner')

print("Merged DataFrame:")
print(merged_df)