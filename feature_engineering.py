from data_cleaning import data_cleaning
from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()
def feat_eng():
    data = data_cleaning()

    columns_to_encode = ['name', 'gender', 'blood_type', 'medical_condition', 'date_of_admission', 'doctor', 'hospital', 'insurance_provider', "admission_type", "medication"]
    for col in columns_to_encode:
        data[col] = label_encoder.fit_transform(data[col])

    data.dtypes

    data.to_csv('final.csv', index=False)

    data.isnull().sum()
    data.duplicated().sum()

    return data


feat_eng()
