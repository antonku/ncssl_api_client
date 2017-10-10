import yaml
import os
from ncssl_api_client.configure import API_CONFIG_PATH, DELIMITER, SETTINGS_FILE_NAME
from ncssl_api_client.configure import main as build_config

home = os.path.expanduser("~")
user_api_settings_path = DELIMITER.join([home, API_CONFIG_PATH, SETTINGS_FILE_NAME])

try:
    with open(user_api_settings_path) as f:
        settings = yaml.load(f)

    locals().update(settings)
except EnvironmentError:  # FileNotFoundError
    build_config()
