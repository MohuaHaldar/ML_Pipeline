from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler

from regression_model.processing import Preprocessors as pp

from regression_model.config import config

titanic_pipe = Pipeline([
    ('Convert_To_Category', pp.ConvertToCategory(variables=config.CONVERT_TO_CAT)),
    ('Categorical_imputer', pp.CategoricalImputer(variables=config.CATEGORICAL_VARIABLES_WITH_NA)),

    ('Numerical_imputer', pp.NumericalImputer(variables=config.NUMERICAL_VARIABLE_WITH_NA)),

    ('Rare_label_converter', pp.RareLabelConverter(pct=1, variables=config.CATEGORICAL_VARS)),
    ('drop_feature', pp.DropUnnecesaryFeature(variables_to_drop=config.DROP_FEATURES)),
    ('categorical_encoder', pp.CategoricalEncoder(variables=config.CATEGORICAL_VARS)),

    ('scale_features', MinMaxScaler()),
    ('LogisticRegression', LogisticRegression(random_state=0))
])
