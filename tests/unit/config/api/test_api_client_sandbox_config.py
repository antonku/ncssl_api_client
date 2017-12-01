import mock
from unittest import TestCase
from ncssl_api_client.config.api.api_client_sandbox_config import ApiSandboxClientConfig


@mock.patch('ncssl_api_client.config.api.api_client_sandbox_config.settings')
@mock.patch('ncssl_api_client.config.api.abstract_api_client_config.settings')
class ApiSandboxClientConfigTest(TestCase):
    api_config_mock = {
        'general': {'sandbox': 'GLOBAL SANDBOX PARAMS TEST'},
        'url': {'sandbox': 'sandbox.example.com'},
        'headers': 'HEADERS TEST',
    }

    def test_ReturnsSandboxGlobalParams(self, abstract_settings_mock, settings_mock):
        settings_mock.client = self.api_config_mock
        abstract_settings_mock.client = self.api_config_mock
        api_sandbox_client_config = ApiSandboxClientConfig()
        global_params = api_sandbox_client_config.get_global_params()
        self.assertEqual(global_params, 'GLOBAL SANDBOX PARAMS TEST')

    def test_ReturnsSandboxUrl(self, abstract_settings_mock, settings_mock):
        settings_mock.client = self.api_config_mock
        abstract_settings_mock.client = self.api_config_mock
        api_sandbox_client_config = ApiSandboxClientConfig()
        url = api_sandbox_client_config.get_api_url()
        self.assertEqual(url, 'sandbox.example.com')

    def test_ReturnsHeaders(self, abstract_settings_mock, settings_mock):
        settings_mock.client = self.api_config_mock
        abstract_settings_mock.client = self.api_config_mock
        api_sandbox_client_config = ApiSandboxClientConfig()
        headers = api_sandbox_client_config.get_headers()
        self.assertEqual(headers, 'HEADERS TEST')


