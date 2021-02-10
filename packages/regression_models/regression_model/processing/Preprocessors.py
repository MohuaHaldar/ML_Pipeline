import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


# categorical missing value imputer

class ConvertToCategory(BaseEstimator, TransformerMixin):
    def __init__(self, variables=None):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        for feature in self.variables:
            X[feature] = X[feature].astype('object')
        #print('Columns after converting to category', X.info())
        return X


class CategoricalImputer(BaseEstimator, TransformerMixin):
    def __init__(self, variables=None):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        for feature in self.variables:
            X[feature] = X[feature].fillna('Missing')

        return X


# class for numeric imputation
class NumericalImputer(BaseEstimator, TransformerMixin):
    def __init__(self, variables=None):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X, y=None):
        self.imputer_dict_ = {}

        for feature in self.variables:
            self.imputer_dict_[feature] = X[feature].mean()
        return self

    def transform(self, X):
        X = X.copy()
        for feature in self.variables:
            X[feature].fillna(self.imputer_dict_[feature], inplace=True)
        return X


class RareLabelConverter(BaseEstimator, TransformerMixin):
    def __init__(self, pct, variables=None):
        self.pct = pct
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X, y=None):
        self.freq_cat = {}

        for feature in self.variables:
            var_freq = pd.Series(100 * X[feature].value_counts() / len(X))
            self.freq_cat[feature] = list(var_freq[var_freq >= self.pct].index)
        return self

    def transform(self, X):
        X = X.copy()
        for feature in self.variables:
            X[feature] = np.where(X[feature].isin(self.freq_cat[feature]), X[feature], 'Rare')
        return X


class CategoricalEncoder(BaseEstimator, TransformerMixin):
    def __init__(self, variables=None):
        if not isinstance(variables, list):
            self.variables = variables
        else:
            self.variables = variables

    def fit(self, X, y=None):
        all_vals = pd.concat([X, y], axis=1)
        #all_vals.columns = X.columns + ['Survived']

        self.enc_dict_ = {}
        for feature in self.variables:
            ord_lbl = all_vals.groupby(feature)['Survived'].mean().sort_values().index
            self.enc_dict_[feature] = {k: i for i, k in enumerate(ord_lbl, 0)}
        return self

    def transform(self, X):
        X = X.copy()
        for var in self.variables:
            X[var] = X[var].map(self.enc_dict_[var])
        return X


class DropUnnecesaryFeature(BaseEstimator, TransformerMixin):
    def __init__(self, variables_to_drop=None):
        self.variables_to_drop = variables_to_drop

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        X.drop(self.variables_to_drop, axis=1, inplace=True)
        return X
