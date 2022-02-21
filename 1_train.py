from joblib import dump
import pandas as pd
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("data/wine.csv")
X = df[df.columns[1:]]
y = df[df.columns[0]]

lr = LogisticRegression(random_state=0, max_iter=100).fit(X, y)
dump(lr, 'models/model.joblib')