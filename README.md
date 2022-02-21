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
* ```dvc run -n train -p train.seed,train.max_iter -d 3_train_pipeline.py -d data/prepared/wine_train.csv -d data/prepared/wine_test.csv -o data/metrics -o models/trained python 3_train_pipeline.py```
* ```dvc run -n evaluate -d 4_evaluate.py -d models/trained/model.joblib -d data/prepared/wine_test.csv -M data/metrics_threshold/scores.json --plots-no-cache data/metrics_threshold/metrics.json python 4_evaluate.py```
* ```dvc repro```
* ```dvc dag```
* ```dvc metrics show```
* ```dvc plots modify data/metrics_threshold/metrics.json -x recall -y precision```
* ```dvc plots show```
* ```dvc params diff```
* ```dvc metrics diff```
* ```dvc plots diff```