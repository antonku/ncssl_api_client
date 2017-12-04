from ncssl_api_client.__main__ import main_cli_wrapper
from unittest import TestCase
import mock


class MainTest(TestCase):

    @mock.patch('ncssl_api_client.__main__.main', return_value=mock.MagicMock())
    def test_status_code_zero_on_success(self, result_mock):
        result_mock().is_successful.return_value = True
        with self.assertRaises(SystemExit) as cm:
            main_cli_wrapper()

        self.assertEqual(cm.exception.code, 0)

    @mock.patch('ncssl_api_client.__main__.main', return_value=mock.MagicMock())
    def test_status_code_one_on_failure(self, result_mock):
        result_mock().is_successful.return_value = False
        with self.assertRaises(SystemExit) as cm:
            main_cli_wrapper()

        self.assertEqual(cm.exception.code, 1)
