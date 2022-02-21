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
* ```dvc run --force -n prepare -p prepare.split -d src/pipeline/prepare.py -d data/wine.csv -o data/prepared python src/pipeline/prepare.py```
* ```dvc run --force -n train -p train.seed,train.max_iter -d src/pipeline/train.py -d data/prepared/wine_train.csv -d data/prepared/wine_test.csv -o metrics/train -o models/trained python src/pipeline/train.py```
* ```dvc run --force -n evaluate -d src/pipeline/evaluate.py -d models/trained/model.joblib -d data/prepared/wine_test.csv -M metrics/test/scores.json --plots-no-cache metrics/test/metrics.json python src/pipeline/evaluate.py```
* ```dvc repro```
* ```dvc dag```
* ```dvc metrics show```
* ```dvc plots modify data/metrics_threshold/metrics.json -x recall -y precision```
* ```dvc plots show```
* ```dvc params diff```
* ```dvc metrics diff```
* ```dvc plots diff```