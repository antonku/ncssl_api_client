import mock
from unittest import TestCase
from ncssl_api_client.config.api import settings

try:
    reload  # Python 2.7
except NameError:
    try:
        from importlib import reload  # Python 3.4+
    except ImportError:
        from imp import reload  # Python 3.0 - 3.3

DATA = 'CRYPTO_SETTINGS_TEST: TEST'


class CryptoSettingsLoadingTest(TestCase):
    @mock.patch("builtins.open", mock.mock_open(read_data=DATA))
    def test_update_locals(self):
        reload(settings)
        self.assertEqual(settings.CRYPTO_SETTINGS_TEST, 'TEST')
