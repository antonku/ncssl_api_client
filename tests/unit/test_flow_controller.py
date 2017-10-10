import logging
import mock
from unittest import TestCase
from ncssl_api_client.flow_controller import FlowController
logging.disable(logging.CRITICAL)


@mock.patch('ncssl_api_client.config.api.api_sandbox_config.ApiSandboxConfig')
@mock.patch('ncssl_api_client.api.api_client.ApiClient')
@mock.patch('ncssl_api_client.crypto.generator.CsrGenerator')
class FlowControllerTest(TestCase):

    supported_operations = (
        'activate',
        'reissue',
        'create',
        'retry_dcv',
        'revoke',
        'renew',
        'create_and_activate',
    )

    def test_throws_error_on_invalid_command(self, csr_generator_mock, api_client_mock, api_config_mock):

        controller = FlowController(api_config_mock, {'common_name': 'example.com'}, api_client_mock, csr_generator_mock)

        with self.assertRaises(AttributeError):
            controller.execute('NON_EXISTENT_COMMAND')

    def test_calls_csr_generator(self, csr_generator_mock, api_client_mock, api_config_mock):

        for command_name in ('activate', 'reissue'):
            # TODO: subTest requires python3.4+, also available in 2.7 if unittest2 is in use
            with self.subTest(command_name=command_name):
                controller = FlowController(api_config_mock, {'common_name': 'example.com'}, api_client_mock, csr_generator_mock)
                controller.execute(command_name)
                csr_generator_mock.generate_csr.assert_called()

    @mock.patch('ncssl_api_client.api.api_response.ApiResponse')
    def test_execute_returns_api_response_instance(self, api_resp_mock, csr_generator_mock, api_client_mock, api_config_mock):

        for command_name in self.supported_operations:
            with self.subTest(command_name=command_name):
                api_client_mock.send_call.return_value = api_resp_mock
                controller = FlowController(api_config_mock, {'common_name': 'example.com'}, api_client_mock, csr_generator_mock)
                result = controller.execute(command_name)
                self.assertEqual(result, api_resp_mock)
