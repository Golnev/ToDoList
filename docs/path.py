from os import path


ROOT_DIR = path.dirname(path.abspath(__file__))

LOGGER_FILE = 'logger_file.log'
PATH_LOGGER = path.join(ROOT_DIR, LOGGER_FILE)  # Path to write logger file.


CONFIG_FILE = 'config.ini'
PATH_CONFIG = path.join(ROOT_DIR, CONFIG_FILE)  # Path to write config file.
