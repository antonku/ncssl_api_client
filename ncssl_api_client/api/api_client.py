import requests
import xmltodict
import logging
import coloredlogs
import json
coloredlogs.install(level='INFO')
# logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


def return_as_dict(method):
    def wrapper(*args):
        return xmltodict.parse(method(*args))

    return wrapper


def api_logger(method):
    def wrapper(*args):
        result = method(*args)
        if result.get('ApiResponse').get('@Status') == 'OK':
            logger.info(json.dumps(result['ApiResponse']['CommandResponse'], indent=2))
        else:
            logger.error(json.dumps(result['ApiResponse']['Errors'], indent=2))
        return result
    return wrapper


class ApiClient:

    def __init__(self, config):
        """
        Api client constructor

        :param config: ApiProductionConfig|ApiSandboxConfig
        """
        self.config = config

    @api_logger
    @return_as_dict
    def send_call(self, params):
        """
        :param params: request payload
        :type params: dict
        :return: api response
        """
        response = requests.post(self.config.get_api_url(), headers=self.config.get_headers(), data=params)
        return response.text
