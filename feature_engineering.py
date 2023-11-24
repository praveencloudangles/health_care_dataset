from data_cleaning import data_cleaning
from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()
def feat_eng():
    data = data_cleaning()

    columns_to_encode = ['name', 'gender', 'blood_type', 'medical_condition', 'date_of_admission', 'doctor', 'hospital', 'insurance_provider', "admission_type", "medication"]
    for col in columns_to_encode:
        data[col] = label_encoder.fit_transform(data[col])

    data.dtypes
    data.isnull().sum()
    data.duplicated().sum()

    data['billing_amount'] = data['billing_amount'].astype('int')

    x = data.drop('test_results', axis=1)
    y = data['test_results']
    oversample = SMOTE()
    X, Y = oversample.fit_resample(x, y)
    data = pd.concat([x, pd.Series(Y, name='test_results')], axis=1)

    data.to_csv('final.csv', index=False)

    return data


feat_eng()
