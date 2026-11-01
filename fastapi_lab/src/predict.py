from pathlib import Path
import joblib
import pandas as pd


MODEL_PATH = (
    Path(__file__).resolve().parent.parent
    / "model"
    / "banknote_model.pkl"
)

artifact = joblib.load(MODEL_PATH)
model = artifact["model"]
feature_names = artifact["features"]


def predict_banknote(variance, skewness, curtosis, entropy):

    values = {
        "variance": variance,
        "skewness": skewness,
        "curtosis": curtosis,
        "entropy": entropy
    }

    features = pd.DataFrame(
        [[values[name] for name in feature_names]],
        columns=feature_names
    )

    prediction = int(model.predict(features)[0])

    probabilities = model.predict_proba(features)[0]
    class_index = list(model.classes_).index(prediction)
    confidence = float(probabilities[class_index])

    return {
        "prediction": prediction,
        "confidence": round(confidence, 4)
    }


