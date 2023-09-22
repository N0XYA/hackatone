import pandas as pd


def remove_duplicates(data_frame):
    data_frame = data_frame.drop_duplicates(subset=["text"], inplace=False, keep='last')
    return data_frame
