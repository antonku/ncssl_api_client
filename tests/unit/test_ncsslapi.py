import logging
import mock
from unittest import TestCase
import argparse
from ncssl_api_client.ncsslapi import main
logging.disable(logging.CRITICAL)


@mock.patch('ncssl_api_client.flow_controller.FlowController.execute')
class CommandLineTest(TestCase):

    @mock.patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(command='getinfo', sandbox=True))
    def test_ExecutesCommand(self, mock_args, controller_execute):
        main()
        controller_execute.assert_called_with('getinfo')

    @mock.patch('ncssl_api_client.config.crypto.crypto_config.CryptoConfig.enable_key_encryption')
    @mock.patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(command='getinfo', sandbox=True, encrypt=True))
    def test_EnabledKeyEncryption(self, mock_args, enable_key_encryption, controller_execute):
        main()
        enable_key_encryption.assert_called_once()

    @mock.patch('ncssl_api_client.config.manager.ConfigManager.get_api_sandbox_client_config')
    @mock.patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(command='getinfo', sandbox=True))
    def test_UsesSandboxApiConfig(self, mock_args, get_api_sandbox_config, controller_execute):
        main()
        get_api_sandbox_config.assert_called_once()

    @mock.patch('ncssl_api_client.config.manager.ConfigManager.get_api_production_client_config')
    @mock.patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(command='getinfo', sandbox=False))
    def test_UsesProductionApiConfig(self, mock_args, get_api_production_config, controller_execute):
        main()
        get_api_production_config.assert_called_once()
