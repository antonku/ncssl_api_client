import unittest
import argparse
from ncssl_api_client.console.parsers.reissue_parser import ReissueParser


class ReissueParserTest(unittest.TestCase):

    def setUp(self):
        self.parser = argparse.ArgumentParser()
        self.subparsers = self.parser.add_subparsers(help='Available commands:', dest='command')
        ReissueParser().add_parser(self.subparsers)

    def test_success_flow(self):
        arguments = self.parser.parse_args([
            'reissue',
            '-cn', 'example.com',
            '-e', 'example@example.com',
            '-id', '0000000',
            '-t', 'PositiveSSL',
            '-y', '1'
        ])
        self.assertEqual(arguments.command, 'reissue')
        self.assertEqual(arguments.sandbox, False)
        self.assertEqual(arguments.ApproverEmail, 'example@example.com')
        self.assertEqual(arguments.CertificateID, '0000000')
        self.assertEqual(arguments.DNSDCValidation, False)
        self.assertEqual(arguments.HTTPDCValidation, False)
        self.assertEqual(arguments.Type.value, 'PositiveSSL')
        self.assertEqual(arguments.common_name, 'example.com')
        self.assertEqual(arguments.encrypt, False)
        self.assertEqual(arguments.Years, 1)

    def test_error_insufficient_args(self):
        with self.assertRaises(SystemExit):
            self.parser.parse_args([
                'reissue',
            ])

    def test_error_invalid_certificate_type(self):
        with self.assertRaises(SystemExit):
            self.parser.parse_args([
                'reissue',
                '-cn', 'example.com',
                '-e', 'example@example.com',
                '-id', '0000000',
                '-t', 'TEST',
                '-y', '1'
            ])

    def test_error_mutually_exclusive_args(self):
        with self.assertRaises(SystemExit):
            self.parser.parse_args([
                'reissue',
                '-cn', 'example.com',
                '-e', 'example@example.com',
                '-dns',
                '-id', '0000000',
                '-t', 'PositiveSSL',
                '-y', '1'
            ])
