import mock
from unittest import TestCase
from ncssl_api_client.api.commands.retry_dcv_command import RetryDcvCommand


@mock.patch('ncssl_api_client.api.api_client.ApiClient')
class RetryDcvCommandTest(TestCase):

    def test_returns_api_response(self, api_client_mock):
        command_params = {}
        api_client_mock.send_call.return_value = 'test api response'
        command = RetryDcvCommand(command_params, api_client_mock)
        result = command.execute()
        self.assertEqual(result, 'test api response')