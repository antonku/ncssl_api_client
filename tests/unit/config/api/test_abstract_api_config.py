import unittest
from ncssl_api_client.config.api.abstract_api_config import AbstractApiConfig


class ApiConfigTest(AbstractApiConfig):

    def __init__(self):
        super(ApiConfigTest, self).__init__()
        self.test_operation_params = {'test_operation': 'TEST TEST TEST'}


class AbstractApiConfigTest(unittest.TestCase):

    def test_magic_method_returns_params(self):

        config = ApiConfigTest()
        params = config.get_test_operation_params()
        self.assertEqual(params['test_operation'], 'TEST TEST TEST')

    def test_magic_method_exception_for_non_existent_params(self):

        with self.assertRaises(AttributeError):
            config = ApiConfigTest()
            config.get_non_existent_operation_params()
