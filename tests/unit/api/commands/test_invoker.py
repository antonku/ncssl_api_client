import mock
from unittest import TestCase
from ncssl_api_client.api.commands.invoker import Invoker
import argparse


@mock.patch('ncssl_api_client.api.commands.invoker.ConfigManager')
@mock.patch('ncssl_api_client.api.commands.invoker.ApiClient')
@mock.patch('ncssl_api_client.api.commands.invoker.Invoker.command_map',
            new_callable=mock.PropertyMock,
            return_value={'mock_command': {'configMethod': 'get_test_params', 'class': mock.MagicMock}})
class InvokerTest(TestCase):

    def test_executes_command(self, command_map_mock, api_client_mock, config_manager_mock):

        mock.MagicMock.execute = lambda x: 'executed'
        arguments_mock = argparse.Namespace(command='mock_command', sandbox=True)
        invoker = Invoker(arguments_mock)
        result = invoker.run()
        self.assertEqual(result, 'executed')

    def test_uses_api_sandbox_client_config(self, command_map_mock, api_client_mock, config_manager_mock):

        mock.MagicMock.execute = lambda x: 'executed'
        arguments_mock = argparse.Namespace(command='mock_command', sandbox=True)
        invoker = Invoker(arguments_mock)
        invoker.run()
        config_manager_mock.get_api_sandbox_client_config.assert_called_once()

    def test_uses_api_production_client_config(self, command_map_mock, api_client_mock, config_manager_mock):

        mock.MagicMock.execute = lambda x: 'executed'
        arguments_mock = argparse.Namespace(command='mock_command', sandbox=False)
        invoker = Invoker(arguments_mock)
        invoker.run()
        config_manager_mock.get_api_production_client_config.assert_called_once()

