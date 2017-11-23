import unittest
import argparse
from ncssl_api_client.console.parsers.create_parser import CreateParser


class CreateParserTest(unittest.TestCase):

    def setUp(self):
        self.parser = argparse.ArgumentParser()
        self.subparsers = self.parser.add_subparsers(help='Available commands:', dest='command')
        CreateParser().add_parser(self.subparsers)

    def test_success_flow(self):
        arguments = self.parser.parse_args(['create', '-y', '1', '-t', 'PositiveSSL'])
        self.assertEqual(arguments.command, 'create')
        self.assertEqual(arguments.sandbox, False)
        self.assertEqual(arguments.Years, 1)
        self.assertEqual(arguments.Type.value, 'PositiveSSL')

    def test_error_invalid_type(self):
        with self.assertRaises(SystemExit):
            self.parser.parse_args(['create', '-t', 'TEST'])
