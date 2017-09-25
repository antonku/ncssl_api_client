from ncssl_api_client.api.api_exception import ApiException


class ApiResponse:

    def __init__(self, response):
        """
        :param response: Raw Api response
        :type response: dict
        """
        self.response = self.validate_response(response)

    @staticmethod
    def validate_response(response):
        if isinstance(response, dict) and ('ApiResponse' in response):
            return response
        raise ApiException('Failed to parse response from API')

    def is_successful(self):
        if self.response['ApiResponse']['@Status'] == 'OK':
            return True
        else:
            return False

    def get_certificate_id(self):

        def find_certificate_id(resp):

            for (key, value) in resp.items():
                if key == "@CertificateID":
                    return int(value)
                elif isinstance(value, dict):
                    return find_certificate_id(value)

        return find_certificate_id(self.response)

    def get_command_response(self):
        return self.response['ApiResponse']['CommandResponse']

    def get_error(self):
        return self.response['ApiResponse']['Errors']
