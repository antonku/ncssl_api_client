import unittest
import argparse
from ncssl_api_client.console.parsers.getinfo_parser import GetInfoParser


class GetInfoParserTest(unittest.TestCase):

    def setUp(self):
        self.parser = argparse.ArgumentParser()
        self.subparsers = self.parser.add_subparsers(help='Available commands:', dest='command')
        GetInfoParser().add_parser(self.subparsers)

    def test_success_flow(self):
        arguments = self.parser.parse_args(['getinfo', '-id', '00000', '-rc'])
        self.assertEqual(arguments.command, 'getinfo')
        self.assertEqual(arguments.ReturnCertificate, True)
        self.assertEqual(arguments.CertificateID, '00000')

    def test_error_insufficient_args(self):
        with self.assertRaises(SystemExit):
            self.parser.parse_args(['getinfo'])
