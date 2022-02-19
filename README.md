* ```dvc init```
* ```dvc add data/wine.csv```
* ```dvc remote add -d myremote gs://test-dvc/```
* ```dvc remote add -d myremote gdrive://1x7syfySLrKBpOCnnW6WXzzTaFX5ElVAW```
* ```dvc push```
* ```dvc pull```
* ```dvc fetch```
* ```dvc checkout```
* ```dvc checkout data/wine.csv```
* ```dvc list https://github.com/sergiorozada12/dvc-walkthrough models```
* ```dvc get https://github.com/sergiorozada12/dvc-walkthrough models/model.joblib```
* ```dvc import https://github.com/sergiorozada12/dvc-walkthrough models/model.joblib```
* ```dvc run -n prepare -p prepare.split -d 2_prepare.py -d data/wine.csv -o data/prepared python 2_prepare.py```