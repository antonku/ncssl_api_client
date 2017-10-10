from ncssl_api_client.config.api.api_production_config import ApiProductionConfig
from ncssl_api_client.config.crypto.crypto_config import CryptoConfig
from ncssl_api_client.config.api.api_sandbox_config import ApiSandboxConfig


class ConfigManager:

    @staticmethod
    def get_api_sandbox_config():
        return ApiSandboxConfig()

    @staticmethod
    def get_api_production_config():
        return ApiProductionConfig()

    @staticmethod
    def get_crypto_config():
        return CryptoConfig()
