import os
import yaml
import pandas as pd


params = yaml.safe_load(open("params.yaml"))["prepare"]
split = params["split"]

os.makedirs(os.path.join("data", "prepared"), exist_ok=True)

df = pd.read_csv("data/wine.csv")
df.iloc[:int(split*df.shape[0])].to_csv("data/prepared/wine_train.csv", index=False)
df.iloc[int(split*df.shape[0]):].to_csv("data/prepared/wine_test.csv", index=False)
