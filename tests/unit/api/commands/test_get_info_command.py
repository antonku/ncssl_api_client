import mock
from unittest import TestCase
from ncssl_api_client.api.commands.get_info_command import GetInfoCommand


@mock.patch('ncssl_api_client.api.api_client.ApiClient')
class GetInfoCommandTest(TestCase):

    def test_returns_api_response(self, api_client_mock):
        command_params = {}
        api_client_mock.send_call.return_value = 'test api response'
        command = GetInfoCommand(command_params, api_client_mock)
        result = command.execute()
        self.assertEqual(result, 'test api response')
