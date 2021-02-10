import pathlib
import regression_model, os

PACKAGE_ROOT = pathlib.Path(regression_model.__file__).resolve().parent
TRAINED_MODEL_DIR = PACKAGE_ROOT / "trained_models"
DATASET_DIR = PACKAGE_ROOT / "datasets"

# data
TRAINING_DATA_FILE = 'train.csv'
TESTING_DATA_FILE = 'test.csv'
TARGET = 'Survived'

# input variables
FEATURES = ['PassengerId', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
            'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
DROP_FEATURES = ['Name', 'PassengerId']
NUMERICAL_VARIABLE_WITH_NA = ['Age']
CONVERT_TO_CAT = ['Sex', 'Embarked']
CATEGORICAL_VARIABLES_WITH_NA = ['Cabin', 'Embarked']
CATEGORICAL_VARS = ['Pclass', 'Sex', 'SibSp', 'Parch', 'Ticket', 'Cabin', 'Embarked']

NUMERICAL_NA_NOT_ALLOWED = [
    feature
    for feature in FEATURES
    if feature not in CATEGORICAL_VARS + NUMERICAL_VARIABLE_WITH_NA
]

CATEGORICAL_NA_NOT_ALLOWED = [
    feature for feature in CATEGORICAL_VARS if feature not in CATEGORICAL_VARIABLES_WITH_NA
]

# pipeline name
PIPELINE_NAME = 'Classification'
# pipeline name
PIPELINE_SAVE_FILE = f"{PIPELINE_NAME}_output_v"

