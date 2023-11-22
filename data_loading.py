import pandas as pd

def data_loading():
    df = pd.read_csv("healthcare_dataset.csv")

    return df

data_loading()