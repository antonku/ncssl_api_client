import os
import logging
from datetime import datetime
from ncssl_api_client.configure import CERTS_PATH, DELIMITER, HOME
logger = logging.getLogger(__name__)


class Utils:

    @staticmethod
    def normalize_cn(common_name):
        return common_name.replace('.', '_').replace('*', 'STAR')

    @staticmethod
    def update_path(common_name):
        dir_name = Utils.normalize_cn(common_name)
        dir_path = DELIMITER.join([HOME, CERTS_PATH, Utils.get_current_year(), dir_name])
        if Utils.create_directory(dir_path) is not True:
            logger.info('Operation has been cancelled by the user')
            exit()

    @staticmethod
    def create_directory(dir_path):
        try:
            os.makedirs(dir_path)
            return True
        except FileExistsError:
            answer = input('\nDirectory "{}" already exists. Do you want to overwrite it contents? (Y/N) '.format(dir_path))
            if answer.lower() == 'yes' or answer.lower() == 'y':
                return True
            return False

    @staticmethod
    def get_current_year():
        return str(datetime.today().year)

    @staticmethod
    def get_csr_as_text(file_name):
        csr_path = DELIMITER.join([Utils.get_cert_dir(file_name), file_name + '.csr'])
        with open(csr_path) as f:
            return f.read()

    @staticmethod
    def get_cert_dir(file_name):
        return DELIMITER.join([HOME, CERTS_PATH, Utils.get_current_year(), file_name])
