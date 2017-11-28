from __future__ import unicode_literals
import os
import logging
from builtins import input
from datetime import datetime
from ncssl_api_client.configure import CERTS_PATH, DELIMITER, HOME
import yaml
import json
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
        except EnvironmentError:  # FileExistsError
            answer = input('\nDirectory "{}" already exists. Do you want to overwrite it contents? (Y/n) '.format(dir_path))
            if answer.lower() == 'yes' or answer.lower() == 'y' or answer.strip() == '':
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

    @staticmethod
    def is_old_style_strings():
        try:
            unicode
        except NameError:
            return False
        return True

    @staticmethod
    def pretty_output(output_data):

        yaml.SafeDumper.org_represent_str = yaml.SafeDumper.represent_str

        def repr_str(dumper, data):
            if Utils.is_old_style_strings():
                data = data.encode('utf-8')
            if '\n' in data:
                return dumper.represent_scalar(u'tag:yaml.org,2002:str', data, style='|')
            if data.startswith('@'):
                return dumper.represent_scalar(u'tag:yaml.org,2002:str', data.replace('@', ''), style='')
            return dumper.org_represent_str(data)

        yaml.add_representer(str, repr_str, Dumper=yaml.SafeDumper)
        if Utils.is_old_style_strings():
            yaml.add_representer(unicode, repr_str, Dumper=yaml.SafeDumper)

        def repr_int(dumper, data):
            return dumper.represent_scalar(u'tag:yaml.org,2002:int', data, style='')

        yaml.add_representer(int, repr_int, Dumper=yaml.SafeDumper)

        json_data = json.loads(json.dumps(output_data))
        return yaml.safe_dump(json_data, indent=2, allow_unicode=True, default_flow_style=False, width=120, default_style='', explicit_start=True)
