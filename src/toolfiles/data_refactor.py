import pandas as pd

df = pd.read_csv("50_rows.csv", low_memory=False)

columns = [column for column in df]

out = pd.DataFrame()
out["channel_id"] = df["channel_id"].values
out["text"] = df["text"].values
out.to_csv (r'../two_columns_50.csv', index= False)
print("done")