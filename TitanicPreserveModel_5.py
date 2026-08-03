import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

#--------------------------------------------------------
#   Function name : PreserveModel
#   Description :   It is used to preserve model on secondary
#   Parameters :    model, filename
#   Return :        None
#   Date :          14/03/2026
#   Author :        Piyush Manohar Khairnar
#--------------------------------------------------------

def PreserveModel(model,filename):
    joblib.dump(model,filename)

    print("Model preserved sucesfully with name : ",filename)

#--------------------------------------------------------
#   Function name : TrainTitanicModel
#   Description :   It does split X, Y, tarinning data ,testing data
#   Parameters :    df
#   Return :        None
#   Date :          14/03/2026
#   Author :        Piyush Manohar Khairnar
#--------------------------------------------------------

def TrainTitanicModel(df):
    # slipt features and labels
    X = df.drop("Survived", axis = 1)
    Y = df["Survived"]

    print("\nFetures : ")
    print(X.head())

    print("\nLabels : ")
    print(Y.head())

    print("Shape of X : ",X.shape)
    print("Shape of Y : ",Y.shape)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)
    print("X_train shape : ",X_train.shape)
    print("X_test shape : ",X_test.shape)
    print("Y_train shape : ",Y_train.shape)
    print("Y_test shape : ",Y_test.shape)

    model = LogisticRegression(max_iter=1000)

    model.fit(X_train,Y_train)
    
    print("Model trained succesfully")

    print("\nIntercept of model : ")
    print(model.intercept_)

    print("\nCoeeficent of model")
    for feature,coeficent in zip(X.columns, model.coef_[0]):
        print(feature, " : ", coeficent)

    PreserveModel(model,"marvelloustitanic.pkl")

#--------------------------------------------------------
#   Function name : DisplayInfo
#   Description :   It displays the formated title
#   Parameters :    title (str)
#   Return :        None
#   Date :          14/03/2026
#   Author :        Piyush Manohar Khairnar
#--------------------------------------------------------

def DisplayInfo(title):
    print("\n" + "="*70)
    print(title)
    print("="*70)

#--------------------------------------------------------
#   Function name : ShowData
#   Description :   It shows basic information about dataset
#   Parameters :    df
#                   df ->       Pandas dataframe object 
#                   message
#                   message ->  Heading text to display
#   Return :        None
#   Date :          14/03/2026
#   Author :        Piyush Manohar Khairnar
#--------------------------------------------------------

def ShowData(df,message):
    DisplayInfo(message)

    print("\nFirst 5 rows of dataset")
    print(df.head())

    print("\nShape of dataset")
    print(df.shape)

    print("\nColumn names : ")
    print(df.columns.tolist())

    print("\nMissing values in each column")
    print(df.isnull().sum())

#--------------------------------------------------------
#   Function name : CleanTitanicData
#   Description :   It does preprocessing
#                   It removed unnecessary columns
#                   It handales missing values
#                   It converts text data to numeric format
#                   It does encoding to categorical columns
#   Parameters :    df ->   Pandas dataframe
#   Return :        df ->   Clean Pandas dataframe
#   Date :          14/03/2026
#   Author :        Piyush Manohar Khairnar
#--------------------------------------------------------

def CleanTitanicData(df):
    DisplayInfo("Step 2 : Original Data")
    print(df.head())

    # Remove unnecessary columns
    drop_columns = ["Passengerid","zero","Name","Cabin"]
    existing_columns = [col for col in drop_columns if col in df.columns]

    print("\n Columns to be dropped : ")
    print(existing_columns)

    # drop the unwated columns
    df = df.drop(columns = existing_columns)
    DisplayInfo("Step 2 : Data after columns removal")
    print(df.head())

    # Handle age column
    if "Age" in df.columns:
        print("Age column before filling missing values")
        print(df["Age"].head(10))

        # coerce -> Invalid value gets converted as NaN
        df["Age"] = pd.to_numeric(df["Age"], errors="coerce")

        age_median = df["Age"].median()
        
        # Replace missing values with median
        df["Age"] = df["Age"].fillna(age_median)

        print("\nAge column after preprocessing : ")
        print(df["Age"].head(10))

    # Handle fare column
    if "Fare" in df.columns:
        print("\n Fare column before preprocessing")
        print(df["Fare"].head(10))

        df["Fare"] = pd.to_numeric(df["Fare"], errors="coerce")
    
        fare_median = df["Fare"].median()
        
        print("\n Meadian of fare column is : ",fare_median)

        # Replace missing values with median
        df["Fare"] = df["Fare"].fillna(fare_median)
        
        print("\Fare column after preprocessing : ")
        print(df["Fare"].head(10))
    
    # Handle Embarked column
    if "Embarked" in df.columns:
        print("\n Embarked column before preprocessing")
        print(df["Embarked"].head(10))

        # convert the data into string
        df["Embarked"] = df["Embarked"].astype(str).str.strip()

        # Remove missing values
        df["Embarked"] = df["Embarked"].replace(['nan','None',''],np.nan)

        # Get most frequent value
        embarked_mode = df["Embarked"].mode()[0]
        print("\nMode of embarked column : ",embarked_mode)

        df["Embarked"] = df["Embarked"].fillna(embarked_mode)

        print("\Embarked column after preprocessing : ")
        print(df["Embarked"].head(10))

    # Handle Sex column
    if "Sex" in df.columns:
        print("\n Sex column before preprocessing")
        print(df["Sex"].head(10))

        df["Sex"] = pd.to_numeric(df["Sex"], errors="coerce")
    
        print("\Sex column after preprocessing : ")
        print(df["Sex"].head(10))

    DisplayInfo("Data after preprocessing")
    print(df.head())

    print("\nMissing values after preprocessing")
    print(df.isnull().sum())
    
    #Encode Embraked column
    df = pd.get_dummies(df,columns=["Embarked"],drop_first=True)
    print("\n Data after encoding")

    print(df.head())

    print("Shape of dataset : ",df.shape)

    # convert boolean columns into integer
    for col in df.columns:
        if df[col].dtype == bool:
            df[col] = df[col].astype(int)

    print("\n Data after encoding")

    print(df.head())

    return df

#--------------------------------------------------------
#   Function name : MarvellousTitanicLogistic
#   Description :   This is main pipeline controller
#                   It loads the dataset, shows raw data
#                   It preprocess the dataset & train the model
#   Parameters :    Data path of dataset file
#   Return :        None
#   Date :          14/03/2026
#   Author :        Piyush Manohar Khairnar
#--------------------------------------------------------

def MarvellousTitanicLogistic(DataPath):
    DisplayInfo("Step 1 : Loading the dataset")
    df = pd.read_csv(DataPath)

    ShowData(df,"Initial dataset")

    df = CleanTitanicData(df)

    TrainTitanicModel(df)


#--------------------------------------------------------
#   Function name : main
#   Description :   Starting point of the application
#   Parameters :    None
#   Return :        None
#   Date :          14/03/2026
#   Author :        Piyush Manohar Khairnar
#--------------------------------------------------------

def main():
    MarvellousTitanicLogistic("MarvellousTitanicDataset.csv")

if __name__ == "__main__":
    main()