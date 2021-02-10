import pandas as pd
import numpy as np
from regression_model.processing.data_management import load_pipeline
from regression_model.config import config
from regression_model.processing.validation import validate_inputs
from regression_model import __version__ as _version
import logging

_logger = logging.getLogger(__name__)

pipeline_file_name = f"{config.PIPELINE_SAVE_FILE}{_version}.pkl"
_titanic_pipe = load_pipeline(file_name=pipeline_file_name)


def make_predictions(*, input_data) -> dict:
    data = pd.DataFrame(input_data)
    validated_data = validate_inputs(input_data=data)
    prediction = _titanic_pipe.predict(validated_data[config.FEATURES])
    response = {"prediction": prediction, "version": _version}

    _logger.info(
        f"Making prediction with model version: {_version}"
        f"Inputs: {validated_data}"
        f"Prediction:{response}"
    )
    return response
