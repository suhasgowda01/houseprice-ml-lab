
"""
Preprocessing pipeline (STARTER)
--------------------------------
TODO: Copy your completed preprocessing code from notebooks/template.ipynb
Section: Feature Engineering & Preprocessing

Required:
- Square root transform on 'sqft'
- OneHotEncoder for ['locality','parking'] (handle_unknown='ignore')
- Pass-through 'bedrooms'
- Treat missing categorical as 'Missing' level (ensure your data has Missing filled)
"""
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import FunctionTransformer, OneHotEncoder
from sklearn.pipeline import Pipeline
import numpy as np

def build_preprocessor():
    # TODO: replace this placeholder ColumnTransformer with your own
    preprocessor = ColumnTransformer(transformers=[
        # ('sqft_sqrt', FunctionTransformer(np.sqrt), ['sqft']),
        # ('cat', OneHotEncoder(handle_unknown='ignore'), ['locality','parking']),
        # ('bedrooms', 'passthrough', ['bedrooms'])
    ])
    return preprocessor
