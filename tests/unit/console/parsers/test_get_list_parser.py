import unittest
import argparse
from ncssl_api_client.console.parsers.get_list_parser import GetListParser


class GetListParserTest(unittest.TestCase):

    def setUp(self):
        self.parser = argparse.ArgumentParser()
        self.subparsers = self.parser.add_subparsers(help='Available commands:', dest='command')
        GetListParser().add_parser(self.subparsers)

    def test_success_flow(self):
        arguments = self.parser.parse_args(['getlist', '-f', 'Processing', '-s', 'PURCHASEDATE', '-kw', 'example.com'])
        self.assertEqual(arguments.command, 'getlist')
        self.assertEqual(arguments.sandbox, False)
        self.assertEqual(arguments.SearchTerm, 'example.com')
        self.assertEqual(arguments.ListType.value, 'Processing')
        self.assertEqual(arguments.SortBy.value, 'PURCHASEDATE')

    def test_error_invalid_filter(self):
        with self.assertRaises(SystemExit):
            self.parser.parse_args(['getlist', '-f', 'TEST'])

    def test_error_invalid_sorter(self):
        with self.assertRaises(SystemExit):
            self.parser.parse_args(['getlist', '-s', 'TEST'])

