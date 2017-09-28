import logging
import mock
from unittest import TestCase
from ncssl_api_client.flow_controller import FlowController
logging.disable(logging.CRITICAL)


@mock.patch('ncssl_api_client.config.api.api_sandbox_config.ApiSandboxConfig')
@mock.patch('ncssl_api_client.api.api_client.ApiClient')
@mock.patch('ncssl_api_client.crypto.generator.CsrGenerator')
class FlowControllerTest(TestCase):

    def test_throws_error_on_invalid_command(self, csr_generator_mock, api_client_mock, api_config_mock):

        controller = FlowController(api_config_mock, {'common_name': 'example.com'}, api_client_mock, csr_generator_mock)

        with self.assertRaises(AttributeError):
            controller.execute('NON_EXISTENT_COMMAND')

    def test_initiates_api_call_on_valid_command(self, csr_generator_mock, api_client_mock, api_config_mock):

        controller = FlowController(api_config_mock, {'common_name': 'example.com'}, api_client_mock, csr_generator_mock)

        # TODO: replace this with some kind of data provider
        for commandName in ('getinfo', 'activate', 'create', 'retry_dcv'):
            controller.execute(commandName)
            api_client_mock.send_call.assert_called()

    def test_activate_command_calls_csr_generator(self, csr_generator_mock, api_client_mock, api_config_mock):

        controller = FlowController(api_config_mock, {'common_name': 'example.com'}, api_client_mock, csr_generator_mock)

        controller.execute('activate')
        csr_generator_mock.generate_csr.assert_called()

    @mock.patch('ncssl_api_client.api.api_response.ApiResponse')
    def test_execute_returns_api_response_instance_on_success(self, api_resp_mock, csr_generator_mock, api_client_mock, api_config_mock):

        api_client_mock.send_call.return_value = api_resp_mock
        controller = FlowController(api_config_mock, {'common_name': 'example.com'}, api_client_mock, csr_generator_mock)

        result = controller.execute('activate')
        self.assertEqual(result, api_resp_mock)







