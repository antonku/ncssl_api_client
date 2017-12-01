import mock
from unittest import TestCase
from ncssl_api_client.config.api.api_client_production_config import ApiProductionClientConfig


@mock.patch('ncssl_api_client.config.api.api_client_production_config.settings')
@mock.patch('ncssl_api_client.config.api.abstract_api_client_config.settings')
class ApiProductionClientConfigTest(TestCase):
    api_config_mock = {
        'general': {'production': 'GLOBAL PRODUCTION PARAMS TEST'},
        'url': {'production': 'production.example.com'},
        'headers': 'HEADERS TEST',
    }

    def test_ReturnsSandboxGlobalParams(self, abstract_settings_mock, settings_mock):
        settings_mock.client = self.api_config_mock
        abstract_settings_mock.client = self.api_config_mock
        api_production_client_config = ApiProductionClientConfig()
        global_params = api_production_client_config.get_global_params()
        self.assertEqual(global_params, 'GLOBAL PRODUCTION PARAMS TEST')

    def test_ReturnsSandboxUrl(self, abstract_settings_mock, settings_mock):
        settings_mock.client = self.api_config_mock
        abstract_settings_mock.client = self.api_config_mock
        api_production_client_config = ApiProductionClientConfig()
        url = api_production_client_config.get_api_url()
        self.assertEqual(url, 'production.example.com')

    def test_ReturnsHeaders(self, abstract_settings_mock, settings_mock):
        settings_mock.client = self.api_config_mock
        abstract_settings_mock.client = self.api_config_mock
        api_production_client_config = ApiProductionClientConfig()
        headers = api_production_client_config.get_headers()
        self.assertEqual(headers, 'HEADERS TEST')


