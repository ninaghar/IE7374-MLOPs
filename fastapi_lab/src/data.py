from ucimlrepo import fetch_ucirepo
from sklearn.model_selection import train_test_split


def get_data():
    # Load UCI Banknote Authentication dataset
    banknote = fetch_ucirepo(id=267)

    X = banknote.data.features
    y = banknote.data.targets.iloc[:, 0].astype(int)

    # Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    return X_train, X_test, y_train, y_test



