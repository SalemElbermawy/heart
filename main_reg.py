import pandas as pd

data=pd.read_excel("threshold_dataset.xlsx")

# print(data.head())


data_x=data.drop("safe_threshold",axis="columns")
data_y=data["safe_threshold"]


from sklearn.model_selection import train_test_split

train_x,test_x,train_y,test_y= train_test_split(data_x,data_y,test_size=0.2,random_state=32)

from sklearn.preprocessing import MinMaxScaler

scaler=MinMaxScaler()

train_x_scalered=scaler.fit_transform(train_x.drop(["has_diabetes","is_smoker"],axis="columns"))

train_x_scalered=pd.DataFrame(train_x_scalered,columns=["age","systolic_bp","diastolic_bp","bmi"])


test_x_scalered=scaler.transform(test_x.drop(["has_diabetes","is_smoker"],axis="columns"))

test_x_scalered=pd.DataFrame(test_x_scalered,columns=["age","systolic_bp","diastolic_bp","bmi"])


# edit data frame

train_x_scalered=pd.concat([train_x_scalered.reset_index(drop=True),train_x[["has_diabetes","is_smoker"]].reset_index(drop=True)],axis=1)


test_x_scalered=pd.concat([test_x_scalered.reset_index(drop=True),test_x[["has_diabetes","is_smoker"]].reset_index(drop=True)],axis=1)



print(train_x_scalered)