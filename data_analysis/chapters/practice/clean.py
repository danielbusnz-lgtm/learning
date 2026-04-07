import pandas as pd

data = {
    'name': ['Alice', 'Bob', 'alice', 'Charlie', 'Bob', None],
    'age': ['25', '30', '25', 'unknown', '30', '40'],
    'country': ['USA', 'U.S.A.', 'USA', 'United States', 'U.S.A.', 'USA'],
    'salary': [50000, 60000, 50000, 70000, 60000, None]
}

df = pd.DataFrame(data)
print("Original data:")
print(df)
print()


df = df.drop_duplicates(subset=['name'])
df['country']= df['country'].replace({'U.S.A.':'USA','United States': 'USA'}) 
df['age']=pd.to_numeric(df['age'],errors='coerce')
df = df.dropna(subset=['name'])

print("Cleaned data:")
print(df)
