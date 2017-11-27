import unittest
import mock
from ncssl_api_client.__main__ import main


@mock.patch('ncssl_api_client.config.manager.ConfigManager.get_crypto_config')
@mock.patch('ncssl_api_client.services.crypto.csr_generator.CsrGenerator.generate_csr')
@mock.patch('ncssl_api_client.api.api_client.ApiClient.send_call', return_value='test api response')
@mock.patch('ncssl_api_client.config.manager.ConfigManager.get_api_command_config')
@mock.patch('ncssl_api_client.config.manager.ConfigManager.get_api_sandbox_client_config')
class ActivateTest(unittest.TestCase):

    def test_success_flow(self, api_config_mock, command_config_mock, api_client_mock, generator, crypto_config_mock):
        with mock.patch('sys.argv', ['ncsslapi', 'activate', '-id', '00000', '-cn', 'example.com', '-http']):
            self.assertEqual(main(), 'test api response')
