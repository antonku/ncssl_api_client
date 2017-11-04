import mock
from unittest import TestCase
from ncssl_api_client.api.commands.reissue_command import ReissueCommand


@mock.patch('ncssl_api_client.api.api_client.ApiClient')
class ReissueCommandTest(TestCase):

    @mock.patch('ncssl_api_client.api.commands.activate_command.CsrGenerator')
    @mock.patch('ncssl_api_client.api.commands.activate_command.ConfigManager')
    def test_returns_api_response(self, csr_generator_mock, config_manager_mock, api_client_mock):
        command_params = {'common_name': 'test'}
        api_client_mock.send_call.return_value = 'test api response'
        command = ReissueCommand(command_params, api_client_mock)
        result = command.execute()
        self.assertEqual(result, 'test api response')