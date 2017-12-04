import mock
from unittest import TestCase

DATA = 'API_SETTINGS_TEST: TEST'


class ApiSettingsLoadingTest(TestCase):
    @mock.patch("builtins.open", mock.mock_open(read_data=DATA))
    def test_update_locals(self):
        import ncssl_api_client.config.api.settings
        self.assertEqual(ncssl_api_client.config.api.settings.API_SETTINGS_TEST, 'TEST')
