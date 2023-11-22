from data_cleaning import data_cleaning
from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()
def feat_eng():
    data = data_cleaning()
    data.replace({'Test Results':{'Normal':0,'Abnormal':1, "Inconclusive":2}},inplace=True)
    print("data------------------",data)

    columns_to_encode = ['Name', 'Gender', 'Blood Type', 'Medical Condition', 'Date of Admission', 'Doctor', 'Hospital', 'Insurance Provider', "Admission Type", "Discharge Date", "Medication"]
    for col in columns_to_encode:
        data[col] = label_encoder.fit_transform(data[col])

    print("data-----", data.dtypes)

    data.to_csv('final.csv', index=False)

    return data


feat_eng()