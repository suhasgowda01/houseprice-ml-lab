
"""
Evaluation script (STARTER)
---------------------------
Usage:
    python -m src.evaluate

TODOs:
- Load model.pkl
- Evaluate on a holdout set (or re-split)
- Print RMSE (and optionally R^2)
"""
import pandas as pd
import numpy as np
import joblib
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

def evaluate(data_path="data/housing.csv", model_path="model.pkl"):
    # TODO: implement evaluation similar to your notebook
    pass

if __name__ == "__main__":
    evaluate()
