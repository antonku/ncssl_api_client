from unittest import TestCase
from ncssl_api_client.services.utils.utils import Utils
from datetime import datetime
import mock

try:
    __import__('__builtin__')
    open_reference = "__builtin__.open"  # Python 2.7
except ImportError:
    open_reference = "builtins.open"  # Python 3.x


class UtilsTest(TestCase):

    def test_normalize_cn(self):
        normalized_common_name = Utils.normalize_cn('*.example.com')
        self.assertEqual(normalized_common_name, 'STAR_example_com')

    def test_get_cert_dir(self):
        cert_dir = Utils.get_cert_dir('example.com')
        self.assertTrue(cert_dir.endswith('ncsslapi/certs/{}/example.com'.format(str(datetime.today().year))))

    @mock.patch(open_reference, mock.mock_open(read_data='base64 data...'))
    def test_returns_csr_as_text(self):
        self.assertEqual(Utils.get_csr_as_text('test'), 'base64 data...')

    def test_adds_csr_extension_to_filename_before_reading(self):
        with mock.patch(open_reference) as mocked_open:
            Utils.get_csr_as_text('test')
            call_arg, _ = mocked_open.call_args
            self.assertTrue(call_arg[0].endswith('test.csr'))
