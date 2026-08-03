import pandas as pd
from sklearn.datasets import fetch_california_housing

data = fetch_california_housing()

df = pd.DataFrame(data.data,columns=data.feature_names)
df["target"] = data.target

df.to_csv("california_housing.csv", index=False)

print("california_housing.csv file gets created succesfully")