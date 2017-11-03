import requests
import xmltodict
import logging
import coloredlogs
import json

from ncssl_api_client.utils.utils import Utils
from ncssl_api_client.api.api_response import ApiResponse
from ncssl_api_client.config.api.api_client_sandbox_config import ApiSandboxClientConfig
from ncssl_api_client.config.api.api_client_production_config import ApiProductionClientConfig
coloredlogs.install(level='INFO')
logger = logging.getLogger(__name__)


def return_as_dict(method):
    def wrapper(*args):
        return xmltodict.parse(method(*args))

    return wrapper


def return_as_api_response(method):
    def wrapper(*args):
        return ApiResponse(method(*args))

    return wrapper


def api_logger(method):
    def wrapper(*args):
        api_response = method(*args)
        if api_response.is_successful():
            command_response = api_response.get_command_response()
            logger.info(Utils.pretty_output(command_response))
        else:
            logger.error(json.dumps(api_response.get_error(), indent=2))
        return api_response
    return wrapper


class ApiClient:

    def __init__(self, config):
        """
        Api client constructor

        :param config: Api client configuration
        :type config: ApiProductionClientConfig|ApiSandboxClientConfig
        """
        self.config = config

    @api_logger
    @return_as_api_response
    @return_as_dict
    def send_call(self, params):
        """
        :param params: request payload
        :type params: dict
        :return: api response
        :type: ApiResponse
        """
        params.update(self.config.global_params)
        response = requests.post(self.config.api_url, headers=self.config.headers, data=params)
        return response.text
