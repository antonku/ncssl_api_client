from ncssl_api_client.config.api.api_client_production_config import ApiProductionClientConfig
from ncssl_api_client.config.crypto.crypto_config import CryptoConfig
from ncssl_api_client.config.api.api_client_sandbox_config import ApiSandboxClientConfig
from ncssl_api_client.config.api.api_command_config import ApiCommandConfig


class ConfigManager:

    @staticmethod
    def get_api_sandbox_client_config():
        return ApiSandboxClientConfig()

    @staticmethod
    def get_api_production_client_config():
        return ApiProductionClientConfig()

    @staticmethod
    def get_api_command_config():
        return ApiCommandConfig()

    @staticmethod
    def get_crypto_config():
        return CryptoConfig()
