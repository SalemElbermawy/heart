import pandas as pd


data= pd.read_excel("dataset.xlsx")

# print(data.head())

# print(data.describe())

# print("\n\n\n ------------------------ \n\n\n")

# print(data.info())

# print("\n\n\n ------------------------ \n\n\n")


# print(data.shape)

# print("\n\n\n ------------------------ \n\n\n")

# data_health=data[data["label"]==0]

# print(data_health.describe())

# print("\n\n\n ------------------------ \n\n\n")

data_x=data.drop("label",axis="columns")
data_y=data["label"]


from sklearn.model_selection import train_test_split

train_x,test_x,train_y,test_y= train_test_split(data_x,data_y,test_size=0.2,random_state=32)

from sklearn.preprocessing import MinMaxScaler

scaler=MinMaxScaler()

train_x_scalered=scaler.fit_transform(train_x.drop(["has_diabetes","is_smoker"],axis="columns"))

train_x_scalered=pd.DataFrame(train_x_scalered,columns=["age","systolic_bp","diastolic_bp","bmi","ir_reading"])


test_x_scalered=scaler.transform(test_x.drop(["has_diabetes","is_smoker"],axis="columns"))

test_x_scalered=pd.DataFrame(test_x_scalered,columns=["age","systolic_bp","diastolic_bp","bmi","ir_reading"])


# edit data frame

train_x_scalered=pd.concat([train_x_scalered.reset_index(drop=True),train_x[["has_diabetes","is_smoker"]].reset_index(drop=True)],axis=1)


test_x_scalered=pd.concat([test_x_scalered.reset_index(drop=True),test_x[["has_diabetes","is_smoker"]].reset_index(drop=True)],axis=1)

# print(data.head())
# print(train_x[["has_diabetes","is_smoker"]])
# print(train_x_scalered)
# print(data.iloc[1868])

# print(test_x_scalered)

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

model.fit(train_x_scalered, train_y)

y_pred = model.predict(test_x_scalered)

accuracy = model.score(test_x_scalered, test_y)

print("Accuracy:", accuracy)

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(test_y, y_pred)

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure()
sns.heatmap(cm, annot=True, fmt='d')
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()


from sklearn.metrics import roc_curve, auc

y_prob = model.predict_proba(test_x_scalered)[:, 1]

fpr, tpr, _ = roc_curve(test_y, y_prob)
roc_auc = auc(fpr, tpr)

plt.figure()
plt.plot(fpr, tpr)
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()
plt.show()