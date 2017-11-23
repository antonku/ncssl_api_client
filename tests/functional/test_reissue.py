import unittest
import mock
import sys
from ncssl_api_client.ncsslapi import main


@mock.patch('ncssl_api_client.config.manager.ConfigManager.get_crypto_config')
@mock.patch('ncssl_api_client.services.crypto.csr_generator.CsrGenerator.generate_csr')
@mock.patch('ncssl_api_client.api.api_client.ApiClient.send_call', return_value='test api response')
@mock.patch('ncssl_api_client.config.manager.ConfigManager.get_api_command_config')
@mock.patch('ncssl_api_client.config.manager.ConfigManager.get_api_sandbox_client_config')
class ReissueTest(unittest.TestCase):

    def test_success_flow(self, api_config_mock, command_config_mock, api_client_mock, generator, crypto_config_mock):
        sys.argv.extend(['reissue', '-id', '00000', '-cn', 'example.com', '-http'])
        self.assertEqual(main(), 'test api response')

    def tearDown(self):
        del sys.argv[1:]
