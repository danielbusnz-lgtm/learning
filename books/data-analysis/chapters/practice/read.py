import json
import pandas as pd

with open("/Users/danielbrooks/learning/data_analysis/chapters/practice/products.json") as f:
    data = json.load(f)
df = pd.json_normalize(data)


print(df)
print(df.dtypes)
