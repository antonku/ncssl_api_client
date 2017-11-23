import unittest
import argparse
from ncssl_api_client.console.parsers.retry_dcv_parser import RetryDcvParser


class RetryDcvParserParserTest(unittest.TestCase):

    def setUp(self):
        self.parser = argparse.ArgumentParser()
        self.subparsers = self.parser.add_subparsers(help='Available commands:', dest='command')
        RetryDcvParser().add_parser(self.subparsers)

    def test_success_flow(self):
        arguments = self.parser.parse_args(['retry_dcv', '-id', '000000'])
        self.assertEqual(arguments.command, 'retry_dcv')
        self.assertEqual(arguments.sandbox, False)
        self.assertEqual(arguments.CertificateID, '000000')

    def test_error_insufficient_args(self):
        with self.assertRaises(SystemExit):
            self.parser.parse_args(['retry_dcv'])
