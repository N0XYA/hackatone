import pandas as pd

df = pd.read_csv('../data.csv', low_memory=False)

output = df.head(50)
output.to_csv (r'../50_rows.csv', index= False )