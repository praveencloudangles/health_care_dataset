from data_loading import data_loading

def data_analysis():
    data = data_loading()
    print("information----------",data.info())
    print("describe----------",data.describe())
    print("column names-----------",data.columns)
    print("shape---------",data.shape)
    print("null values--------------",data.isnull().sum())
    for col in data.columns:
        print(col, data[col].nunique())

    print("duplicate values---------",data.describe().sum())
    return data
data_analysis()