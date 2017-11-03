import logging
import mock
from unittest import TestCase
from ncssl_api_client.api.api_client import ApiClient
from ncssl_api_client.api.api_response import ApiResponse
logging.disable(logging.CRITICAL)


class ApiClientTest(TestCase):

    @mock.patch('ncssl_api_client.config.api.api_client_sandbox_config.ApiSandboxClientConfig')
    @mock.patch('requests.post')
    def test_ReturnsApiResponse(self, request_post, api_config):
        request_post.return_value.text = '<ApiResponse Status="OK"><CommandResponse></CommandResponse></ApiResponse>'
        api_client = ApiClient(api_config)
        response = api_client.send_call({})
        self.assertIsInstance(response, ApiResponse)
