import os
import pickle

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer

DATA_DIR = "/opt/airflow/data"
WORKING_DIR = "/opt/airflow/working_data"
MODEL_DIR = "/opt/airflow/model"

os.makedirs(WORKING_DIR, exist_ok=True)
os.makedirs(MODEL_DIR, exist_ok=True)


def load_data():
    """Load the UCI Red Wine Quality dataset."""
    csv_path = os.path.join(DATA_DIR, "winequality-red.csv")

    df = pd.read_csv(csv_path, sep=";")

    # Create a binary classification target.
    # 1 = quality >= 6, 0 = quality < 6
    df["good_quality"] = (df["quality"] >= 6).astype(int)

    out_path = os.path.join(WORKING_DIR, "raw.pkl")
    with open(out_path, "wb") as f:
        pickle.dump(df, f)

    print(f"Loaded {len(df)} wine records")
    return out_path


def data_preprocessing(file_path):
    """Prepare features and split the dataset."""
    with open(file_path, "rb") as f:
        df = pickle.load(f)

    X = df.drop(columns=["quality", "good_quality"])
    y = df["good_quality"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.3,
        random_state=42,
        stratify=y,
    )

    out_path = os.path.join(
        WORKING_DIR, "preprocessed.pkl"
    )

    with open(out_path, "wb") as f:
        pickle.dump(
            (X_train, X_test, y_train, y_test), f
        )

    print("Data preprocessing completed")
    return out_path


def separate_data_outputs(file_path):
    """Pass the prepared data path to the next task."""
    return file_path


def build_model(file_path, filename):
    """Train and save a Random Forest classifier."""
    with open(file_path, "rb") as f:
        X_train, X_test, y_train, y_test = pickle.load(f)

    model = make_pipeline(
        SimpleImputer(strategy="median"),
        RandomForestClassifier(
            n_estimators=100,
            random_state=42,
        ),
    )

    model.fit(X_train, y_train)

    model_path = os.path.join(MODEL_DIR, filename)

    with open(model_path, "wb") as f:
        pickle.dump(model, f)

    print(f"Model saved to {model_path}")
    return model_path


def load_model(file_path, filename):
    """Load the model and calculate evaluation metrics."""
    with open(file_path, "rb") as f:
        X_train, X_test, y_train, y_test = pickle.load(f)

    model_path = os.path.join(MODEL_DIR, filename)

    with open(model_path, "rb") as f:
        model = pickle.load(f)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(
        y_test, predictions, zero_division=0
    )
    recall = recall_score(
        y_test, predictions, zero_division=0
    )
    f1 = f1_score(
        y_test, predictions, zero_division=0
    )

    print(f"Accuracy:  {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall:    {recall:.4f}")
    print(f"F1 Score:  {f1:.4f}")

    return {
        "accuracy": float(accuracy),
        "precision": float(precision),
        "recall": float(recall),
        "f1_score": float(f1),
    }


# # File: src/model_development.py
# import os
# import pickle
# import pandas as pd
# from sklearn.compose import make_column_transformer
# from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import MinMaxScaler, StandardScaler

# WORKING_DIR = "/opt/airflow/working_data"
# MODEL_DIR = "/opt/airflow/model"
# os.makedirs(WORKING_DIR, exist_ok=True)
# os.makedirs(MODEL_DIR, exist_ok=True)

# def load_data() -> str:
#     """
#     Load CSV and persist raw dataframe to a pickle file.
#     Returns path to saved file.
#     """
#     csv_path = os.path.join(
#         os.path.dirname(os.path.dirname(__file__)),
#         "data",
#         "advertising.csv",
#     )
#     df = pd.read_csv(csv_path)

#     out_path = os.path.join(WORKING_DIR, "raw.pkl")
#     with open(out_path, "wb") as f:
#         pickle.dump(df, f)
#     return out_path

# def data_preprocessing(file_path: str) -> str:
#     """
#     Load dataframe, split, scale, and save (X_train, X_test, y_train, y_test) to pickle.
#     Returns path to saved file.
#     """
#     with open(file_path, "rb") as f:
#         df = pickle.load(f)

#     X = df.drop(
#         ["Timestamp", "Clicked on Ad", "Ad Topic Line", "Country", "City"],
#         axis=1,
#     )
#     y = df["Clicked on Ad"]

#     X_train, X_test, y_train, y_test = train_test_split(
#         X, y, test_size=0.3, random_state=42
#     )

#     num_columns = [
#         "Daily Time Spent on Site",
#         "Age",
#         "Area Income",
#         "Daily Internet Usage",
#         "Male",
#     ]

#     ct = make_column_transformer(
#         (MinMaxScaler(), num_columns),
#         (StandardScaler(), num_columns),
#         remainder="passthrough",
#     )

#     X_train_tr = ct.fit_transform(X_train)
#     X_test_tr = ct.transform(X_test)

#     out_path = os.path.join(WORKING_DIR, "preprocessed.pkl")
#     with open(out_path, "wb") as f:
#         pickle.dump((X_train_tr, X_test_tr, y_train.values, y_test.values), f)
#     return out_path

# def separate_data_outputs(file_path: str) -> str:
#     """
#     Passthrough; kept so the DAG composes cleanly.
#     """
#     return file_path

# def build_model(file_path: str, filename: str) -> str:
#     """
#     Train LR model and save to MODEL_DIR/filename. Returns model path.
#     """
#     with open(file_path, "rb") as f:
#         X_train, X_test, y_train, y_test = pickle.load(f)

#     model = LogisticRegression()
#     model.fit(X_train, y_train)

#     model_path = os.path.join(MODEL_DIR, filename)
#     with open(model_path, "wb") as f:
#         pickle.dump(model, f)

#     return model_path

# def load_model(file_path: str, filename: str) -> int:
#     """
#     Load saved model and test set, print score, and return first prediction as int.
#     """
#     with open(file_path, "rb") as f:
#         X_train, X_test, y_train, y_test = pickle.load(f)

#     model_path = os.path.join(MODEL_DIR, filename)
#     with open(model_path, "rb") as f:
#         model = pickle.load(f)

#     score = model.score(X_test, y_test)
#     print(f"Model score on test data: {score}")

#     pred = model.predict(X_test)
#     return int(pred[0])
