import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,recall_score,precision_score,f1_score
from sklearn.model_selection import train_test_split
from dvclive import Live

import yaml

def train():
    print("Training model...")
    data_path = os.path.dirname(__file__) + "/../data/prepared/prepared_iris.csv"
    data = pd.read_csv(data_path)
    X = data.drop("variety", axis=1)
    y = data["variety"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    params = yaml.safe_load(open("params.yaml"))["train"]
    with Live() as live:

        live.log_param("n_estimators", params["n_estimators"])

        clf = RandomForestClassifier(n_estimators=params["n_estimators"])
        clf.fit(X_train, y_train)

        y_train_pred = clf.predict(X_train)

        live.log_metric("train/f1", f1_score(y_train, y_train_pred, average="weighted"), plot=False)
        live.log_metric("train/accuracy", accuracy_score(y_train, y_train_pred), plot=False)
        live.log_metric("train/recall", recall_score(y_train, y_train_pred, average="weighted"), plot=False)
        live.log_metric("train/precision", precision_score(y_train, y_train_pred, average="weighted"), plot=False)
        live.log_sklearn_plot(
            "confusion_matrix", y_train, y_train_pred, name="train/confusion_matrix",
            title="Train Confusion Matrix")

        y_test_pred = clf.predict(X_test)

        live.log_metric("test/f1", f1_score(y_test, y_test_pred, average="weighted"), plot=False)
        live.log_metric("test/accuracy", accuracy_score(y_test, y_test_pred), plot=False)
        live.log_metric("test/recall", recall_score(y_test, y_test_pred, average="weighted"), plot=False)
        live.log_metric("test/precision", precision_score(y_test, y_test_pred, average="weighted"), plot=False)
        live.log_sklearn_plot(
            "confusion_matrix", y_test, y_test_pred, name="test/confusion_matrix",
            title="Test Confusion Matrix")
        
if __name__ == "__main__":
    train()