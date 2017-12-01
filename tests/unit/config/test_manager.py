import mock
from unittest import TestCase
from ncssl_api_client.config.manager import ConfigManager


class ConfigManagerTest(TestCase):

    def setUp(self):
        self.cfg_manager = ConfigManager()

    @mock.patch('ncssl_api_client.config.manager.ApiSandboxClientConfig', return_value='TEST')
    def test_ReturnsApiSandboxClientConfigInstance(self, api_sandbox_client_config_mock):
        config = self.cfg_manager.get_api_sandbox_client_config()
        self.assertEqual(config, 'TEST')

    @mock.patch('ncssl_api_client.config.manager.ApiProductionClientConfig', return_value='TEST')
    def test_ReturnsApiProductionClientConfigInstance(self, api_production_client_config_mock):
        config = self.cfg_manager.get_api_production_client_config()
        self.assertEqual(config, 'TEST')

    @mock.patch('ncssl_api_client.config.manager.ApiCommandConfig', return_value='TEST')
    def test_ReturnsApiCommandConfigInstance(self, api_command_config_mock):
        config = self.cfg_manager.get_api_command_config()
        self.assertEqual(config, 'TEST')

    @mock.patch('ncssl_api_client.config.manager.CryptoConfig', return_value='TEST')
    def test_ReturnsCryptoConfigInstance(self, crypto_config_mock):
        config = self.cfg_manager.get_crypto_config()
        self.assertEqual(config, 'TEST')
