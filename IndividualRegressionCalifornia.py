import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import BaggingRegressor
from sklearn.metrics import mean_squared_error, r2_score

#---------------------------------------------
# Step 1 : Load the dataset
#---------------------------------------------

df = pd.read_csv("california_housing.csv")
print("Shape of dataset : ",df.shape)
print("First 5 records : ",df.head())

#---------------------------------------------
# Step 2 : Separate fetures and labels
#---------------------------------------------

X = df.drop("target",axis=1)
Y = df["target"]

#---------------------------------------------
# Step 3 : Split dataset for tarining and testing
#---------------------------------------------
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

#---------------------------------------------
# Step 4 : Create Base model
#---------------------------------------------
model = DecisionTreeRegressor(random_state=42)

#---------------------------------------------
# Step 5 : Train model
#---------------------------------------------

model.fit(X_train,Y_train)

#---------------------------------------------
# Step 6 : Test  model
#---------------------------------------------

Y_pred = model.predict(X_test)

#---------------------------------------------
# Step 7 : Evaluate Bagging model
#---------------------------------------------

print("MeanSquaredError : ",mean_squared_error(Y_test, Y_pred))

print("R Square : ",r2_score(Y_test, Y_pred))