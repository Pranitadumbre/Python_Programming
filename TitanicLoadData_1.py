import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

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