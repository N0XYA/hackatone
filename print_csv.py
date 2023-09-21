import pandas as pd

def p_head():
    df = pd.read_csv("data.csv", low_memory=False)
    df_head = df["text"].head()
    df_head = df_head.tolist()
    return df_head
