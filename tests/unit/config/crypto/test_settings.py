import mock
from unittest import TestCase

DATA = 'CRYPTO_SETTINGS_TEST: TEST'


class CryptoSettingsLoadingTest(TestCase):
    @mock.patch("builtins.open", mock.mock_open(read_data=DATA))
    def test_update_locals(self):
        import ncssl_api_client.config.crypto.settings
        self.assertEqual(ncssl_api_client.config.crypto.settings.CRYPTO_SETTINGS_TEST, 'TEST')