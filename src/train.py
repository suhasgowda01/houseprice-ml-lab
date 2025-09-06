
"""
Training script (STARTER)
-------------------------
TODOs:
1) Load data from data/housing.csv (or your CSV)
2) Fill NA in 'locality' and 'parking' with 'Missing'
3) Split X (features) and y (target='rent')
4) train_test_split
5) Build pipeline: preprocessor -> LinearRegression
6) Fit, evaluate (RMSE), and joblib.dump(model, 'model.pkl')
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.pipeline import Pipeline
import joblib

from .preprocess import build_preprocessor

def train(data_path="data/housing.csv", model_path="model.pkl"):
    # TODO: Load CSV
    # df = pd.read_csv(data_path)

    # TODO: Fill NA in categorical as 'Missing'
    # df['locality'] = df['locality'].fillna('Missing')
    # df['parking']  = df['parking'].fillna('Missing')

    # TODO: Split features/target
    # y = df['rent']
    # X = df.drop(columns=['rent'])

    # TODO: Split
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Build pipeline
    preprocessor = build_preprocessor()
    model = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', LinearRegression())
    ])

    # TODO: Fit
    # model.fit(X_train, y_train)

    # TODO: Evaluate
    # y_pred = model.predict(X_test)
    # rmse = mean_squared_error(y_test, y_pred, squared=False)
    # print("RMSE:", rmse)

    # TODO: Save
    # joblib.dump(model, model_path)
    # print(f"Saved model to {model_path}")  # double braces to avoid f-string eval

if __name__ == "__main__":
    train()
