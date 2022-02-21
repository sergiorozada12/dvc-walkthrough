import json
from joblib import load
import pandas as pd
from sklearn import metrics
import math
import os

os.makedirs(os.path.join("metrics", "test"), exist_ok=True)

model = load("models/trained/model.joblib")

df_test = pd.read_csv("data/prepared/wine_test.csv")
X_test = df_test[df_test.columns[1:]]
y_test = (df_test[df_test.columns[0]] == 3)*1

y_pred = model.predict_proba(X_test)[:, 2]
pre, rec, th = metrics.precision_recall_curve(y_test, y_pred)

y_pred_labels = (model.predict(X_test) == 3)*1
acc_avg = metrics.accuracy_score(y_test, y_pred_labels)
pre_avg = metrics.precision_score(y_test, y_pred_labels, average='micro')
rec_avg = metrics.recall_score(y_test, y_pred_labels, average='micro')

# General metrics
with open('metrics/test/scores.json', 'w') as f:
    json.dump({"accuracy": acc_avg, "precision": pre_avg, "recall": rec_avg}, f)

# Metrics by threshohld
nth_point = math.ceil(len(th)/1000)
test_results = list(zip(pre, rec, th))[::nth_point]
with open("metrics/test/metrics.json", "w") as f:
    json.dump(
        {"prc": [{"precision": p, "recall": r, "threshold": t} for p, r, t in test_results]},
        f,
        indent=4,
    )
