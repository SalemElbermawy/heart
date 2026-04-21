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



from sklearn.linear_model import Ridge, RidgeCV
from sklearn.metrics import mean_squared_error,r2_score




# model=RidgeCV(alphas=[0.1,1,10,0.01,100,0.001])

# model.fit(train_x_scalered,train_y)

# y_predict=model.predict(test_x_scalered)
# print(model.alpha_)

# print(mean_squared_error(test_y,y_predict))
# print(r2_score(test_y,y_predict))


model=Ridge(alpha=0.1)

model.fit(train_x_scalered,train_y)

y_predict=model.predict(test_x_scalered)

print(mean_squared_error(test_y,y_predict))
print(r2_score(test_y,y_predict))

# import matplotlib.pyplot as plt

# plt.scatter(test_y, y_predict)
# plt.xlabel("Actual Values")
# plt.ylabel("Predicted Values")
# plt.title("Actual vs Predicted")

# plt.plot([test_y.min(), test_y.max()],
#          [test_y.min(), test_y.max()],
#          color='red')

# plt.show()


# from sklearn.model_selection import learning_curve

# train_sizes, train_scores, test_scores = learning_curve(
#     model, train_x_scalered, train_y, cv=5
# )

# plt.plot(train_sizes, train_scores.mean(axis=1), label="Train")
# plt.plot(train_sizes, test_scores.mean(axis=1), label="Test")

# plt.xlabel("Training Size")
# plt.ylabel("Score")
# plt.title("Learning Curve")
# plt.legend()
# plt.show()

# print(train_x_scalered.head())

def prediction_function(age,systolic_bp,diastolic_bp,bmi,has_diabetes,is_smoker):
    
    

    test=pd.DataFrame([[age,systolic_bp,diastolic_bp,bmi,has_diabetes,is_smoker]],columns=["age","systolic_bp","diastolic_bp","bmi","has_diabetes","is_smoker"])
    train_x_scalered_test=scaler.transform(test.drop(["has_diabetes","is_smoker"],axis="columns"))

    train_x_scalered_test=pd.DataFrame(train_x_scalered_test,columns=["age","systolic_bp","diastolic_bp","bmi"])
    
    train_x_scalered_test=pd.concat([train_x_scalered_test.reset_index(drop=True),test[["has_diabetes","is_smoker"]].reset_index(drop=True)],axis=1)
    
    return train_x_scalered_test

# print(prediction_function(69,193,106,26.9,0,0))
    
    
print(model.predict(prediction_function(69,193,106,26.5,0,0)))
print(data.head())