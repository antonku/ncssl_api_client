import os
from shutil import copyfile

BASE_DIR = 'ncsslapi'
CERTS_DIR = 'certs'
CONFIG_DIR = 'config'
API_DIR = 'api'
CRYPTO_DIR = 'crypto'
SETTINGS_FILE_NAME = 'settings.yaml'
DELIMITER = '/'

CONFIG_PATH = DELIMITER.join([BASE_DIR, CONFIG_DIR])
CERTS_PATH = DELIMITER.join([BASE_DIR, CERTS_DIR])
API_CONFIG_PATH = DELIMITER.join([CONFIG_PATH, API_DIR])
CRYPTO_CONFIG_PATH = DELIMITER.join([CONFIG_PATH, CRYPTO_DIR])

package_dir = os.path.dirname(os.path.realpath(__file__))


def setup_layout():
    if not os.path.isdir(BASE_DIR):
        os.mkdir(BASE_DIR)
    if not os.path.isdir(CONFIG_PATH):
        os.mkdir(CONFIG_PATH)
    if not os.path.isdir(API_CONFIG_PATH):
        os.mkdir(API_CONFIG_PATH)
    if not os.path.isdir(CRYPTO_CONFIG_PATH):
        os.mkdir(CRYPTO_CONFIG_PATH)
    if not os.path.isdir(CERTS_PATH):
        os.mkdir(CERTS_PATH)


def setup_configs():
    user_api_config_path = DELIMITER.join([API_CONFIG_PATH, SETTINGS_FILE_NAME])
    if not os.path.exists(user_api_config_path):
        # TODO: ask questions
        source_api_config = DELIMITER.join([package_dir, CONFIG_DIR, API_DIR, SETTINGS_FILE_NAME])
        copyfile(source_api_config, user_api_config_path)

    user_crypto_config_path = DELIMITER.join([CRYPTO_CONFIG_PATH, SETTINGS_FILE_NAME])
    if not os.path.exists(user_crypto_config_path):
        # TODO: ask questions
        source_crypto_config = DELIMITER.join([package_dir, CONFIG_DIR, CRYPTO_DIR, SETTINGS_FILE_NAME])
        copyfile(source_crypto_config, user_crypto_config_path)


def setup_user_directory():

    home = os.path.expanduser("~")
    os.chdir(home)
    setup_layout()
    setup_configs()

