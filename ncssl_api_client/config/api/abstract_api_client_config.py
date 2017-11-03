from abc import ABCMeta
from future.utils import with_metaclass

from ncssl_api_client.config.api import settings


class AbstractApiClientConfig(with_metaclass(ABCMeta)):
    def __init__(self):
        self.global_params = None
        self.api_url = None
        self.headers = settings.client['headers']

    def get_global_params(self):
        return self.global_params

    def get_api_url(self):
        return self.api_url

    def get_headers(self):
        return self.headers
