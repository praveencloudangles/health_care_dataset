from data_analysis import data_analysis
import seaborn as sns
import matplotlib as plt
import pandas as pd
from imblearn.over_sampling import SMOTE

def data_cleaning():
    data = data_analysis()
    data.dropna(inplace=True)
    data.isnull().sum()
    data.drop_duplicates(inplace=True)
    data.duplicated().sum()
    data.columns = data.columns.str.lower().str.replace(' ', '_')
    data.drop('discharge_date', inplace=True, axis=1)
    data.replace({'test_results':{'Normal':0,'Abnormal':1, "Inconclusive":2}},inplace=True)

    return data

data_cleaning()
