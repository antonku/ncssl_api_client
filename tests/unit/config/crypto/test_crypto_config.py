import mock
from unittest import TestCase
from ncssl_api_client.config.crypto.crypto_config import CryptoConfig


@mock.patch('ncssl_api_client.config.crypto.crypto_config.settings')
class CryptoConfigTest(TestCase):

    def test_ReturnsCsrSubject(self, settings_mock):
        settings_mock.csr_subject = 'SUBJECT TEST'
        crypto_config = CryptoConfig()
        subject = crypto_config.get_csr_subject()
        self.assertEqual(subject, 'SUBJECT TEST')

    def test_ReturnsKeySize(self, settings_mock):
        settings_mock.key_size = 512
        crypto_config = CryptoConfig()
        key_size = crypto_config.get_key_size()
        self.assertEqual(key_size, 512)

    def test_ReturnsKeyEncryptionAlgorithm(self, settings_mock):
        settings_mock.key_encryption_algorithm = 'TEST123'
        crypto_config = CryptoConfig()
        key_encryption_algorithm = crypto_config.get_key_encryption_algorithm()
        self.assertEqual(key_encryption_algorithm, 'TEST123')

    def test_ReturnsKeyEncryptionStatus(self, settings_mock):
        crypto_config = CryptoConfig()
        self.assertFalse(crypto_config.key_encryption_enabled())

    def test_EnablesKeyEncryption(self, settings_mock):
        crypto_config = CryptoConfig()
        crypto_config.enable_key_encryption()
        self.assertTrue(crypto_config.key_encryption_enabled())



