from sklearn.model_selection import train_test_split
from regression_model import pipeline
from regression_model.processing.data_management import load_dataset, save_pipeline
from regression_model.config import config


def run_training() -> None:
    data = load_dataset(file_name=config.TRAINING_DATA_FILE)
    # divide train and test set
    x_train, x_test, y_train, y_test = train_test_split(data[config.FEATURES], data[config.TARGET], test_size=.2,
                                                        random_state=0)
    pipeline.titanic_pipe.fit(x_train[config.FEATURES], y_train)
    # joblib.dump(pipeline.titanic_pipe, config.PIPELINE_NAME)
    save_pipeline(pipeline_to_save=pipeline.titanic_pipe)


if __name__ == '__main__':
    run_training()
