import os
import json
import yaml
from joblib import dump
import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, recall_score, precision_score

params = yaml.safe_load(open("params.yaml"))["train"]
seed = params["seed"]

os.makedirs(os.path.join("data", "metrics"), exist_ok=True)
os.makedirs(os.path.join("models", "trained"), exist_ok=True)

df_train = pd.read_csv("data/prepared/wine_train.csv")
df_test = pd.read_csv("data/prepared/wine_test.csv")

X_train = df_train[df_train.columns[1:]]
y_train = df_train[df_train.columns[0]]

X_test = df_test[df_test.columns[1:]]
y_test = df_test[df_test.columns[0]]


lr = LogisticRegression(random_state=seed, max_iter=10000).fit(X_train, y_train)

y_pred = lr.predict(X_test)
acc = accuracy_score(y_test, y_pred)
pre = precision_score(y_test, y_pred, average='micro')
rec = recall_score(y_test, y_pred, average='micro')

dump(lr, 'models/trained/model.joblib')
with open('data/metrics/metrics.json', 'w') as f:
    json.dump({"accuracy": acc, "precision": pre, "recall": rec}, f)
