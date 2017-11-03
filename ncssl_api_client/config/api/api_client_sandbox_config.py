from ncssl_api_client.config.api.abstract_api_client_config import AbstractApiClientConfig
from ncssl_api_client.config.api import settings


class ApiSandboxClientConfig(AbstractApiClientConfig):
    def __init__(self):
        super(ApiSandboxClientConfig, self).__init__()
        self.global_params = settings.client['general']['sandbox']
        self.api_url = settings.client['url']['sandbox']