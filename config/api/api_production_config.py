from config.api.abstract_api_config import AbstractApiConfig
from config.api import settings


class ApiProductionConfig(AbstractApiConfig):
    def __init__(self):
        super(ApiProductionConfig, self).__init__()
        self.global_params = settings.general['production']
        self.api_url = settings.url['production']