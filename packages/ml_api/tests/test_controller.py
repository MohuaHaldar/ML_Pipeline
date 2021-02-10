from regression_model.processing.data_management import load_dataset
from regression_model import __version__ as _version
import json
from regression_model.config import config as model_config
from api import __version__ as api_version


def test_health_endpoint_returns_200(flask_test_client):
    # When
    response = flask_test_client.get('/health')
    # Then
    assert response.status_code == 200


def test_version_endpoint_returns_version(flask_test_client):
    # When
    response = flask_test_client.get('/version')

    # Then
    assert response.status_code == 200
    response_json = json.loads(response.data)
    assert response_json['model_version'] == _version
    assert response_json['api_version'] == api_version


# def test_prediction_endpoint_returns_prediction(flask_test_client):
#     # read the test data from ml_model package
#     test_data = load_dataset(file_name=model_config.TESTING_DATA_FILE)
#     post_json = test_data[0:1].to_json(orient='records')
#
#     # When
#     response = flask_test_client.post('/v1/predict/regression', json=post_json)
#
#     # Then
#     assert response.status_code == 200
#     response_data = json.load(response.data)
#     version = response_data['version']
#     assert version == _version
