import os
import logging
logger = logging.getLogger(__name__)


class Utils:

    @staticmethod
    def normalize_cn(common_name):
        return common_name.replace('.', '_').replace('*', 'STAR')

    @staticmethod
    def update_path(common_name):
        dir_name = Utils.normalize_cn(common_name)
        if Utils.create_directory(dir_name) is True:
            os.chdir(dir_name)
        else:
            logger.info('Operation has been cancelled by the user')
            exit()

    @staticmethod
    def create_directory(dir_name):
        try:
            os.mkdir(dir_name)
            return True
        except FileExistsError:
            answer = input('\nDirectory "{}" already exists. Do you want to overwrite it contents? (Y/N) '.format(dir_name))
            if answer.lower() == 'yes' or answer.lower() == 'y':
                return True
            return False
