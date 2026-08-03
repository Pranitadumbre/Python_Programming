import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score, classification_report,confusion_matrix

#---------------------------------------------
# Step 1 : Load the dataset
#---------------------------------------------

df = pd.read_csv("breast_cancer.csv")
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
# Step 4 : Create Booting Model (AdaBoost)
#---------------------------------------------
boost_model = AdaBoostClassifier(
    n_estimators=50,
    learning_rate=1.0,
    random_state=42)

#---------------------------------------------
# Step 5 : Train Boosting model
#---------------------------------------------

boost_model.fit(X_train,Y_train)

#---------------------------------------------
# Step 6 : Test Boosting model
#---------------------------------------------

Y_pred = boost_model.predict(X_test)

#---------------------------------------------
# Step 7 : Evaluate Boosting model
#---------------------------------------------

print("Boosting Accuracy : ",accuracy_score(Y_test,Y_pred))

print("Confustion matrix : ")
print(confusion_matrix(Y_test,Y_pred))