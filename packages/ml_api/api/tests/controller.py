from flask import Blueprint, request, jsonify
from api.config import get_logger
from regression_model.predict import make_predictions
from api import __version__ as api_version
from regression_model import __version__ as model_version
from api.validation import validate_inputs

_logger = get_logger(logger_name=__name__)

prediction_app = Blueprint('prediction_app', __name__)


@prediction_app.route('/health', methods=['GET'])
def health():
    if request.method == 'GET':
        _logger.info('health status ok')
        return 'ok'


# Adding a version endpoint
@prediction_app.route('/version', methods=['GET'])
def version():
    if request.method == 'GET':
        return jsonify({'model_version': model_version, 'api_version': api_version})


# Adding a prediction endpoint
@prediction_app.route('/v1/predict/regression', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Step 1: Extract post data as JSON body
        json_data = request.get_json()
        #_logger.debug(f"Inputs : {json_data}")

        # Step 2: Validate the input using mashmallow schema
        input_data, errors = validate_inputs(input_data=json_data)

        # Step 3: Model prediction
        # we do not keep any feature engg code in the api to keep it light weights
        result = make_predictions(input_data=input_data)
        _logger.info(f"Outputs : {result}")
        # Convert to list
        prediction = result.get('prediction').tolist()
        version_val = result.get('version')
        return jsonify({'prediction': prediction, 'version': version_val,
                        'errors': errors})
