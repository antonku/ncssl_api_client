import unittest
from ncssl_api_client.api.api_response import ApiResponse
from ncssl_api_client.api.api_exception import ApiException


class ApiResponseTest(unittest.TestCase):

    def test_returns_certificate_id(self):

        response_data = {
            "ApiResponse": {
                "@Type": "namecheap.ssl.create",
                "SSLCreateResult": {
                    "@IsSuccess": "true",
                    "@OrderId": "1030907",
                    "@TransactionId": "1519287",
                    "@ChargedAmount": "9.0000",
                    "SSLCertificate": {
                        "@CertificateID": "909327",
                        "@Created": "09/25/2017",
                        "@SSLType": "PositiveSSL",
                        "@Years": "1",
                        "@Status": "NewPurchase"
                    }
                }
            }
        }

        api_response = ApiResponse(response_data)
        cert_id = api_response.get_certificate_id()

        self.assertEqual(909327, cert_id)

    def test_throws_exception_on_invalid_response(self):

        with self.assertRaises(ApiException):
            ApiResponse('TEST INVALID PARAMETER')

    def test_returns_error(self):

        response_data = {
            "ApiResponse": {
                "@Status": "ERROR",
                "@xmlns": "http://api.namecheap.com/xml.response",
                "Errors": {
                    "Error": {
                        "@Number": "2011294",
                        "#text": "CertificateId is not valid"
                    }
                },
                "RequestedCommand": "namecheap.ssl.getInfo",
                "CommandResponse": {}
            },
        }

        api_response = ApiResponse(response_data)
        self.assertEqual(response_data['ApiResponse']['Errors'], api_response.get_error())

    def test_returns_command_response(self):

        response_data = {
            "ApiResponse": {
                "@Status": "ERROR",
                "@xmlns": "http://api.namecheap.com/xml.response",
                "RequestedCommand": "namecheap.ssl.getInfo",
                "CommandResponse": {
                    "@Type": "namecheap.ssl.getInfo",
                    "SSLGetInfoResult": {
                        "@Years": "0",
                        "@OrderId": "0",
                        "@SANSCount": "0"
                    }
                },
            }
        }

        api_response = ApiResponse(response_data)
        self.assertEqual(response_data['ApiResponse']['CommandResponse'], api_response.get_command_response())

    def test_returns_response_status_success(self):

        response_data = {
            "ApiResponse": {
                "@Status": "ERROR",
            }
        }

        api_response = ApiResponse(response_data)
        self.assertFalse(api_response.is_successful())

    def test_returns_response_status_error(self):

        response_data = {
            "ApiResponse": {
                "@Status": "OK",
            }
        }

        api_response = ApiResponse(response_data)
        self.assertTrue(api_response.is_successful())
