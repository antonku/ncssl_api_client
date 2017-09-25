import logging
from unittest import TestCase

import mock

from ncssl_api_client.flow_controller import FlowController

logging.disable(logging.CRITICAL)


@mock.patch('ncssl_api_client.config.api.api_sandbox_config.ApiSandboxConfig')
@mock.patch('ncssl_api_client.config.crypto.crypto_config.CryptoConfig')
class FlowControllerTest(TestCase):

    def test_throws_error_on_invalid_command(self, mock_api_config, mock_crypto_config):

        controller = FlowController(mock_api_config, mock_crypto_config, {'common_name': 'example.com'})

        with self.assertRaises(AttributeError):
            controller.execute('NON_EXISTENT_COMMAND')

    @mock.patch('ncssl_api_client.api.api_client.ApiClient')
    @mock.patch('ncssl_api_client.crypto.generator.CsrGenerator')
    def test_initiates_api_call_on_valid_command(self, mock_api_config, mock_crypto_config, mock_api_client, mock_csr_generator):

        controller = FlowController(mock_api_config, mock_crypto_config, {'common_name': 'example.com'})

        controller.api_client = mock_api_client
        controller.generator = mock_csr_generator

        for commandName in ('getinfo', 'activate', 'create', 'retry_dcv'):
            controller.execute(commandName)
            controller.api_client.send_call.assert_called()

    @mock.patch('ncssl_api_client.api.api_client.ApiClient')
    @mock.patch('ncssl_api_client.crypto.generator.CsrGenerator')
    def test_activate_command_calls_csr_generator(self, mock_api_config, mock_crypto_config, mock_api_client, mock_csr_generator):

        controller = FlowController(mock_api_config, mock_crypto_config, {'common_name': 'example.com'})

        controller.api_client = mock_api_client
        controller.generator = mock_csr_generator

        controller.execute('activate')
        controller.generator.generate_csr.assert_called()






