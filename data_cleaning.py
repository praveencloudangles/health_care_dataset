from data_analysis import data_analysis

def data_cleaning():
    data = data_analysis()
    data.dropna(inplace=True)
    data.isnull().sum()
    data.drop_duplicates(inplace=True)
    print("-----------------",data.duplicated().sum())
    print(data.dtypes)
    return data

data_cleaning()