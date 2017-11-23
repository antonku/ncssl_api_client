import unittest
import argparse
from ncssl_api_client.console.parsers.revoke_parser import RevokeParser


class RevokeParserParserTest(unittest.TestCase):

    def setUp(self):
        self.parser = argparse.ArgumentParser()
        self.subparsers = self.parser.add_subparsers(help='Available commands:', dest='command')
        RevokeParser().add_parser(self.subparsers)

    def test_success_flow(self):
        arguments = self.parser.parse_args(['revoke', '-id', '000000', '-t', 'PositiveSSL'])
        self.assertEqual(arguments.command, 'revoke')
        self.assertEqual(arguments.sandbox, False)
        self.assertEqual(arguments.CertificateID, '000000')
        self.assertEqual(arguments.CertificateType.value, 'PositiveSSL')

    def test_error_insufficient_args(self):
        with self.assertRaises(SystemExit):
            self.parser.parse_args(['revoke'])

    def test_error_invalid_cert_type(self):
        with self.assertRaises(SystemExit):
            self.parser.parse_args(['renew', '-t', 'TEST', '-id', '000000'])

