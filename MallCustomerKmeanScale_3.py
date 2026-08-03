import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def main():
    #-------------------------------------
    # Step 1 : Load the dataset
    #-------------------------------------
    print("Step 1 : Load the dataset")
    df = pd.read_csv("Mall_Customers.csv")

    print("First few records : ")
    print(df.head())

    print("Shape of dataset : ")
    print(df.shape)

    print("Missing values : ")
    print(df.isnull().sum())

    #-------------------------------------
    # Step 2 : Select Fetures (Independent)
    #-------------------------------------

    print("Step 2 : Select Fetures (Independent)")

    X = df[["AnnualIncome", "SpendingScore"]]
    print("Selected fetures : ")
    print(X.head())

    print("Shape of selected fetures : ")
    print(X.shape)
    
    #-------------------------------------
    # Step 3 : Scale the data
    #-------------------------------------

    scalar = StandardScaler()
    X_scaled = scalar.fit_transform(X)

    print("Data after scalling : ")
    print(X_scaled[:5])



if __name__ == "__main__":
    main()
