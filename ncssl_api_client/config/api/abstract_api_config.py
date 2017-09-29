from abc import ABCMeta

from ncssl_api_client.config.api import settings


class AbstractApiConfig(metaclass=ABCMeta):
    def __init__(self):
        self.global_params = None
        self.api_url = None
        self.create_params = settings.create
        self.activate_params = settings.activate
        self.reissue_params = settings.reissue
        self.getinfo_params = settings.getinfo
        self.retry_dcv_params = settings.retry_dcv
        self.renew_params = settings.renew
        self.revoke_params = settings.revoke
        self.getlist_params = settings.getlist
        self.getemaillist_params = settings.get_email_list
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

    def get_reissue_params(self):
        params = self.global_params.copy()
        params.update(self.reissue_params)
        return params

    def get_getinfo_params(self):
        params = self.global_params.copy()
        params.update(self.getinfo_params)
        return params

    def get_retry_dcv_params(self):
        params = self.global_params.copy()
        params.update(self.retry_dcv_params)
        return params

    def get_renew_params(self):
        params = self.global_params.copy()
        params.update(self.renew_params)
        return params

    def get_revoke_params(self):
        params = self.global_params.copy()
        params.update(self.revoke_params)
        return params

    def get_getlist_params(self):
        params = self.global_params.copy()
        params.update(self.getlist_params)
        return params

    def get_email_list_params(self):
        params = self.global_params.copy()
        params.update(self.getemaillist_params)
        return params

    def get_headers(self):
        return self.headers

