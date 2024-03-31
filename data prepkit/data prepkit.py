import numpy as np
import pandas as pd

file_path=input("plz,enter your file path : ")
def read_file (file_path):
    file_exet=file_path.split(".")[-1]
    if file_exet == "csv":
        dataset=pd.read_csv(file_path)
        return dataset
    elif file_exet == "json":
        dataset=pd.read_json(file_path)
        return dataset
    elif file_exet == ["xlsx","xls"]:
        dataset=pd.read_excel(file_path)
        return dataset
    else :
        print("unsupported file")
data=read_file(file_path)
df=pd.DataFrame(data)
df



def data_info(df):
    integer_col=df.select_dtypes(include='int')
    data_summary={'mean':np.mean(integer_col,axis=0),'median':np.median(integer_col,axis=0),'max':np.max(integer_col,axis=0),'min':np.min(integer_col,axis=0),'std':np.std(integer_col,axis=0)}
    return pd.DataFrame(data_summary)
data_summary=data_info(df)
data_summary
df.describe()
df.head(10)
df.tail(10)
df.shape



handel_method=input("enter your handel method [drop/mean] : ")
def handel_func(df,handel_method):
    integer_col=df.select_dtypes(include='int')
    if handel_method=='mean':
        return df.fillna(integer_col.mean())
    elif handel_method=='drop':
        return df.dropna()
    else:
        print("you are not select the method")
cleand_data=handel_func(df,handel_method)
cleand_data



from sklearn.preprocessing import LabelEncoder
data_type=df.dtypes
categorical=data_type[data_type=='object'].index.tolist()
label_encoder=LabelEncoder()
for column in categorical:
    df[column]=label_encoder.fit_transform(df[column])
df