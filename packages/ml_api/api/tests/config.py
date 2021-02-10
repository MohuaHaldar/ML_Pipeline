import logging
from logging.handlers import TimedRotatingFileHandler
import pathlib, os, sys

PACKAGE_ROOT = pathlib.Path(__file__).resolve().parent.parent
print(PACKAGE_ROOT)
FORMATTER = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s -"
    "%(funcName)s:%(lineno)d - %(message)s"
)
LOG_DIR = PACKAGE_ROOT / 'logs'
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / 'ml_api.log'


# method for writing logs into the console
def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler


# write logs into files
def get_file_handler():
    file_handler = TimedRotatingFileHandler(LOG_FILE, when='midnight')
    file_handler.setFormatter(FORMATTER)
    file_handler.setLevel(logging.WARNING)
    return file_handler


def get_logger(*, logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler())
    logger.propagate = False
    return logger


class Config:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this_needs_to_be_set'
    SERVER_PORT = 5000


class ProductionConfig(Config):
    DEBUG = False
    SERVER_PORT = os.environ.get('PORT', 5000)


class DevelopmentConfig(Config):
    DEBUG = False
    DEVELOPMENT = True


class TestingConfig(Config):
    TESTING = True
