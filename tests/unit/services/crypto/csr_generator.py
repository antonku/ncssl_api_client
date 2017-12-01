import mock
from unittest import TestCase
from ncssl_api_client.services.crypto.csr_generator import CsrGenerator


class CsrGeneratorTest(TestCase):

    @mock.patch('ncssl_api_client.services.crypto.csr_generator.Utils')
    def test_generates_private_key(self, utils_mock):
        crypto_config_mock = mock.MagicMock()
        crypto_config_mock.get_key_size.return_value = 2048
        crypto_config_mock.key_encryption_enabled.return_value = False
        crypto_config_mock.get_subject.return_value = {}
        utils_mock.normalize_cn = lambda x: x.replace('.', '_')
        utils_mock.get_cert_dir.return_value = ''
        utils_mock.update_path.return_value = None

        with mock.patch('ncssl_api_client.services.crypto.csr_generator.CsrGenerator.openssl_exec') as openssl_exec_mock:
            csr_generator = CsrGenerator(crypto_config_mock)
            csr_generator.generate_csr('test.example.com')
            self.assertEqual(csr_generator.openssl_exec.call_args_list[0],
                             mock.call(['genrsa', '-out', '/test_example_com.key', '2048']))

    @mock.patch('ncssl_api_client.services.crypto.csr_generator.Utils')
    def test_generates_encrypted_private_key(self, utils_mock):
        crypto_config_mock = mock.MagicMock()
        crypto_config_mock.get_key_size.return_value = 2048
        crypto_config_mock.key_encryption_enabled.return_value = True
        crypto_config_mock.get_subject.return_value = {}
        crypto_config_mock.get_key_encryption_algorithm.return_value = '-aes256'
        utils_mock.normalize_cn = lambda x: x.replace('.', '_')
        utils_mock.get_cert_dir.return_value = ''
        utils_mock.update_path.return_value = None

        with mock.patch('ncssl_api_client.services.crypto.csr_generator.CsrGenerator.openssl_exec') as openssl_exec_mock:
            csr_generator = CsrGenerator(crypto_config_mock)
            csr_generator.generate_csr('test.example.com')
            self.assertEqual(csr_generator.openssl_exec.call_args_list[0],
                             mock.call(['genrsa', '-aes256', '-out', '/test_example_com.key', '2048']))

    @mock.patch('ncssl_api_client.services.crypto.csr_generator.Utils')
    def test_generates_csr(self, utils_mock):
        crypto_config_mock = mock.MagicMock()
        crypto_config_mock.get_key_size.return_value = 2048
        crypto_config_mock.key_encryption_enabled.return_value = False
        crypto_config_mock.get_subject.return_value = {}
        utils_mock.normalize_cn = lambda x: x.replace('.', '_')
        utils_mock.get_cert_dir.return_value = ''
        utils_mock.update_path.return_value = None

        with mock.patch('ncssl_api_client.services.crypto.csr_generator.CsrGenerator.openssl_exec') as openssl_exec_mock:
            csr_generator = CsrGenerator(crypto_config_mock)
            csr_generator.generate_csr('test.example.com')
            self.assertEqual(csr_generator.openssl_exec.call_args_list[1],
                             mock.call(['req', '-new', '-key', '/test_example_com.key', '-out', '/test_example_com.csr', '-subj', '/']))
