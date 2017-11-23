import unittest
import argparse
from ncssl_api_client.console.parsers.get_email_list_parser import GetEmailListParser


class GetEmailListParserTest(unittest.TestCase):

    def setUp(self):
        self.parser = argparse.ArgumentParser()
        self.subparsers = self.parser.add_subparsers(help='Available commands:', dest='command')
        GetEmailListParser().add_parser(self.subparsers)

    def test_success_flow(self):
        arguments = self.parser.parse_args(['get_email_list', '-t', 'PositiveSSL', '-d', 'example.com'])
        self.assertEqual(arguments.command, 'get_email_list')
        self.assertEqual(arguments.sandbox, False)
        self.assertEqual(arguments.CertificateType.value, 'PositiveSSL')
        self.assertEqual(arguments.DomainName, 'example.com')

    def test_error_insufficient_args(self):
        with self.assertRaises(SystemExit):
            self.parser.parse_args(['create'])

    def test_error_invalid_cert_type(self):
        with self.assertRaises(SystemExit):
            self.parser.parse_args(['create', '-t', 'TEST', '-d', 'example.com'])
