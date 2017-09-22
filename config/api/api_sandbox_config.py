from config.api.abstract_api_config import AbstractApiConfig
from config.api import settings


class ApiSandboxConfig(AbstractApiConfig):
    def __init__(self):
        super(ApiSandboxConfig, self).__init__()
        self.global_params = settings.general['sandbox']
        self.api_url = settings.url['sandbox']