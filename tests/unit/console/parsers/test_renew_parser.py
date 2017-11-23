import unittest
import argparse
from ncssl_api_client.console.parsers.renew_parser import RenewParser


class RenewParserParserTest(unittest.TestCase):

    def setUp(self):
        self.parser = argparse.ArgumentParser()
        self.subparsers = self.parser.add_subparsers(help='Available commands:', dest='command')
        RenewParser().add_parser(self.subparsers)

    def test_success_flow(self):
        arguments = self.parser.parse_args(['renew', '-t', 'PositiveSSL', '-id', '000000', '-y', '1'])
        self.assertEqual(arguments.command, 'renew')
        self.assertEqual(arguments.sandbox, False)
        self.assertEqual(arguments.SSLType.value, 'PositiveSSL')
        self.assertEqual(arguments.CertificateID, '000000')
        self.assertEqual(arguments.Years, 1)

    def test_error_insufficient_args(self):
        with self.assertRaises(SystemExit):
            self.parser.parse_args(['renew'])

    def test_error_invalid_cert_type(self):
        with self.assertRaises(SystemExit):
            self.parser.parse_args(['renew', '-t', 'TEST', '-id', '000000', '-y', '1'])
