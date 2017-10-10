import yaml
import os
from ncssl_api_client.configure import CRYPTO_CONFIG_PATH, DELIMITER, SETTINGS_FILE_NAME
from ncssl_api_client.configure import main as build_config

home = os.path.expanduser("~")
user_crypto_settings_path = DELIMITER.join([home, CRYPTO_CONFIG_PATH, SETTINGS_FILE_NAME])

try:
    with open(user_crypto_settings_path) as f:
        settings = yaml.load(f)

    locals().update(settings)
except EnvironmentError:  # FileNotFoundError
    build_config()
