import unittest
from ncssl_api_client.validator import Validator


class ValidatorTest(unittest.TestCase):

    def test_validates_certificate_type_invalid(self):

        with self.assertRaises(ValueError):
            Validator.validate_certificate_type('TEST TEST TEST')

    def test_returns_certificate_type_valid(self):

        valid_type = Validator.validate_certificate_type('positivessl')
        self.assertEqual('PositiveSSL', valid_type)

    def test_validates_sorter_invalid(self):

        with self.assertRaises(ValueError):
            Validator.validate_sorter('TEST TEST TEST')

    def test_returns_sorter_valid(self):

        valid_sorter = Validator.validate_sorter('expiredatetime')
        self.assertEqual('EXPIREDATETIME', valid_sorter)

    def test_validates_filter_invalid(self):

        with self.assertRaises(ValueError):
            Validator.validate_filter('TEST TEST TEST')

    def test_returns_filter_valid(self):

        valid_filter = Validator.validate_filter('aCtIve')
        self.assertEqual('Active', valid_filter)
