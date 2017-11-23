import os
import yaml
import ipgetter
from shutil import copyfile
from builtins import input
from getpass import getpass
from pprint import pprint

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

HOME = os.path.expanduser("~")
PACKAGE_DIR = os.path.dirname(os.path.realpath(__file__))


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


def update_with_user_api_info(settings):

    client_ip = ipgetter.myip()
    client_ip_input = input('Your external IP address seems to be [{}].\n'
                            'Press <Enter> if it\'s ok, otherwise, '
                            'enter the correct one manually: '.format(client_ip))
    if client_ip_input:
        client_ip = client_ip_input

    for env in ['production', 'sandbox']:
        settings['client']['general'][env]['ClientIp'] = client_ip
        settings['client']['general'][env]['UserName'] = input('Enter Namecheap {} username: '.format(env))
        settings['client']['general'][env]['ApiUser'] = settings['client']['general'][env]['UserName']
        settings['client']['general'][env]['ApiKey'] = getpass('Enter Namecheap {} api key: '.format(env))

    admin_email = input('Enter email address certificates should be sent to: ')
    for command in ['activate', 'reissue']:
        settings['command'][command]['AdminEmailAddress'] = admin_email

    return settings


def setup_configs():
    user_api_config_path = DELIMITER.join([API_CONFIG_PATH, SETTINGS_FILE_NAME])
    if not os.path.exists(user_api_config_path):
        source_api_config_path = DELIMITER.join([PACKAGE_DIR, CONFIG_DIR, API_DIR, SETTINGS_FILE_NAME])
        with open(source_api_config_path) as f:
            source_api_config = yaml.load(f)
            api_config = update_with_user_api_info(source_api_config)
            stream = open(user_api_config_path, 'w')
            yaml.dump(api_config, stream, default_flow_style=False, indent=4, width=79)

    user_crypto_config_path = DELIMITER.join([CRYPTO_CONFIG_PATH, SETTINGS_FILE_NAME])
    if not os.path.exists(user_crypto_config_path):
        # TODO: ask questions
        source_crypto_config_path = DELIMITER.join([PACKAGE_DIR, CONFIG_DIR, CRYPTO_DIR, SETTINGS_FILE_NAME])
        copyfile(source_crypto_config_path, user_crypto_config_path)


def main():
    if os.getenv('NCSSLAPIENV', 'PRODUCTION') != 'TEST':
        print('*** Application seems to be unconfigured ***')
        print('~~~~~~~~~~~~~~~~~~~~~~~~CONFIGURING~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
        os.chdir(HOME)
        setup_layout()
        setup_configs()
        print('\n~~~~~~~~~~~~~~~~~~~~CONFIGURATION FINISHED~~~~~~~~~~~~~~~~~~~~')
        print('*** Application is ready for use ***')
        exit()
