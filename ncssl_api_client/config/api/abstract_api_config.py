from abc import ABCMeta
from future.utils import with_metaclass

from ncssl_api_client.config.api import settings


class AbstractApiConfig(with_metaclass(ABCMeta)):
    def __init__(self):

        self.global_params = {}
        self.api_url = None
        self.headers = settings.headers
        self.create_params = settings.create
        self.activate_params = settings.activate
        self.reissue_params = settings.reissue
        self.getinfo_params = settings.getinfo
        self.retry_dcv_params = settings.retry_dcv
        self.renew_params = settings.renew
        self.revoke_params = settings.revoke
        self.getlist_params = settings.getlist
        self.getemaillist_params = settings.get_email_list

    def __getattr__(self, method_name):

        def gather_operation_params():
            operation_name = '_'.join(method_name.split('_')[1:])
            operation_params = getattr(self, operation_name)
            operation_params.update(self.global_params.copy())
            return operation_params

        if method_name.startswith('get') and method_name.endswith('params'):
            return gather_operation_params

        raise AttributeError

    def get_global_params(self):
        return self.global_params

    def get_api_url(self):
        return self.api_url

    def get_headers(self):
        return self.headers

