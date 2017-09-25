from abc import ABCMeta

from ncssl_api_client.config.api import settings


class AbstractApiConfig(metaclass=ABCMeta):
    def __init__(self):
        self.global_params = None
        self.api_url = None
        self.create_params = settings.create
        self.activate_params = settings.activate
        self.getinfo_params = settings.getinfo
        self.headers = settings.headers

    def get_global_params(self):
        return self.global_params

    def get_api_url(self):
        return self.api_url

    def get_create_params(self):
        params = self.global_params.copy()
        params.update(self.create_params)
        return params

    def get_activate_params(self):
        params = self.global_params.copy()
        params.update(self.activate_params)
        return params

    def get_getinfo_params(self):
        params = self.global_params.copy()
        params.update(self.getinfo_params)
        return params

    def get_headers(self):
        return self.headers

