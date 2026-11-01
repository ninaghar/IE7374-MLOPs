from pathlib import Path
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

from data import get_data


def train_model():
    X_train, X_test, y_train, y_test = get_data()

    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=10,
        random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    print(f"Model Accuracy: {accuracy:.4f}")
    print(classification_report(y_test, predictions))

    model_path = (
        Path(__file__).resolve().parent.parent
        / "model"
        / "banknote_model.pkl"
    )

    model_path.parent.mkdir(parents=True, exist_ok=True)

    joblib.dump({
        "model": model,
        "features": X_train.columns.tolist(),
        "accuracy": accuracy
    }, model_path)

    print(f"Model saved to: {model_path}")


if __name__ == "__main__":
    train_model()

