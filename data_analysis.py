from data_loading import data_loading

def data_analysis():
    data = data_loading()
    data.info()
    data.describe()
    data.columns
    data.shape
    data.isnull().sum()
    for col in data.columns:
        print(col, data[col].nunique())

    data.describe().sum()
    return data
data_analysis()
