# Breast Cancer Classification with MLflow

## Overview
This project demonstrates an end-to-end machine learning workflow using the Wisconsin Diagnostic Breast Cancer dataset and MLflow. It covers exploratory data analysis, model training and comparison, hyperparameter tuning, experiment tracking, model registration, batch inference, and local REST API serving.



## Dataset
- **Source:** Wisconsin Diagnostic Breast Cancer dataset, accessed through `sklearn.datasets.load_breast_cancer`.
- **Samples:** 569
- **Features:** 30 numeric measurements
- **Target:** `malignant` — `1` = malignant, `0` = benign (re-encoded from scikit-learn's original target).
- **Missing values:** None in the loaded dataset.

The dataset is split into approximately 70% training, 15% validation, and 15% held-out testing, with stratification by target class.

## Models and evaluation
The notebook trains and compares:
1. Logistic Regression with standardized features (baseline)
2. Random Forest
3. Gradient Boosting
4. Logistic Regression with cross-validated regularization tuning

Model selection is based on validation ROC-AUC. The selected model is refitted using the training and validation data, then evaluated on the held-out test set. Metrics include accuracy, precision, recall, F1, ROC-AUC, and a confusion matrix.

### Initial validation comparison
| Model | Accuracy | Precision | Recall | F1 | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression baseline | 0.976744 | 0.968750 | 0.968750 | 0.968750 | 0.998843 |
| Random Forest | 0.953488 | 0.966667 | 0.906250 | 0.935484 | 0.997106 |
| Gradient Boosting | 0.965116 | 0.967742 | 0.937500 | 0.952381 | 0.996528 |

These are **validation** metrics, not final test results. See the notebook and MLflow runs for tuning and final test metrics.

## MLflow workflow
- Logs experiment parameters, evaluation metrics, and trained model artifacts.
- Registers the selected final model as `BreastCancerClassifier` in MLflow Model Registry.
- Loads a registered model version for inference.
- Saves batch predictions to `breast_cancer_batch_predictions.csv`.
- Produces a confusion-matrix plot and a top-feature plot.
- Demonstrates local model serving and HTTP prediction requests.

## Project files
| File | Purpose |
|---|---|
| `breast_cancer_mlflow.ipynb` | End-to-end notebook |
| `requirements.txt` | Python dependencies |
| `breast_cancer_batch_predictions.csv` | Example batch inference output |
| `breast_cancer_confusion_matrix.png` | Final test-set confusion matrix |
| `breast_cancer_feature_importance.png` | Feature influence visualization |

## Setup
Use Python with an isolated virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
jupyter notebook
```

Open `breast_cancer_mlflow.ipynb` and run the cells in order. The dataset is bundled with scikit-learn and does not require a separate CSV download.

## View MLflow experiments
From the project directory, run:

```bash
mlflow ui --port 5000
```

Open <http://127.0.0.1:5000>. When using a custom tracking URI or backend store, configure the UI and notebook to point to the same store.

## Serve the registered model
After running the notebook and registering the model, start a second terminal using the same Python environment and MLflow tracking store:

```bash
mlflow models serve -m "models:/BreastCancerClassifier/1" -p 5001 --env-manager local
```

Replace `1` with the actual registered model version. The endpoint is `http://127.0.0.1:5001/invocations` and accepts MLflow `dataframe_split` JSON input with the same feature columns as the training data. See the notebook for an example request.

## Limitations
- The dataset is relatively small; results depend on the data split and should not be interpreted as clinical performance.
- Built-in tree importances and absolute standardized Logistic Regression coefficients have different interpretations and are not causal explanations.
- Batch inference here uses pandas and CSV output.
- MLflow run artifacts and local registry state are not committed to Git; reproduce them by running the notebook with a correctly configured tracking store.
