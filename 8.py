import pandas as pd

# Create a dictionary
data = {
    'Name': ['Sreenath', 'Bobby', 'Paardhu', 'Kamal'],
    'Age': [18, 19, 18, 17],
    'City': ['Karimnagar', 'Hyderabad', 'Warangal', 'Nizamabad']
}

df_from_dict = pd.DataFrame(data)

print("DataFrame from Dictionary:")
print(df_from_dict)
