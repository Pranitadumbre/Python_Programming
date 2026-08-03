import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def MarvellousClassifier(DataPath):
    border = "-"*40

    # Step 1 : Load the dataset from CSV file

    print(border)
    print("Step 1 : Load the dataset from CSV file")
    print(border)
    
    df = pd.read_csv(DataPath)
    print(border)
    print("Some entries from from dataset")
    print(df.head())
    print(border)

    # Step 2 : Clean the dataset by removing empty rows
    print(border)
    print("Step 2 : Clean the dataset by removing empty rows")
    print(border)

    df.dropna(inplace=True)
    print("Total records : ",df.shape[0])
    print("Total columns : ",df.shape[1])
    print(border)

def main():
    border = "-"*40
    print(border)
    print("Wine Classifier using KNN")
    print(border)

    MarvellousClassifier("WinePredictor.csv")
    
if __name__ == "__main__":
    main()