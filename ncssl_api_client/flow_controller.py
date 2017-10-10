import logging

from ncssl_api_client.api.api_client import ApiClient
from ncssl_api_client.config.api.api_sandbox_config import ApiSandboxConfig
from ncssl_api_client.crypto.csr_generator import CsrGenerator
from ncssl_api_client.api.api_response import ApiResponse

logger = logging.getLogger(__name__)


class FlowController:

    OPERATION_NAME_CREATE_AND_ACTIVATE = 'create_and_activate'
    OPERATION_NAME_ACTIVATE = 'activate'
    OPERATION_NAME_CREATE = 'create'
    OPERATION_NAME_GETINFO = 'getinfo'
    OPERATION_NAME_RETRY_DCV = 'retry_dcv'
    OPERATION_NAME_REISSUE = 'reissue'
    OPERATION_NAME_RENEW = 'renew'
    OPERATION_NAME_REVOKE = 'revoke'
    OPERATION_NAME_GET_LIST = 'getlist'
    OPERATION_NAME_GET_EMAIL_LIST = 'get_email_list'

    def __init__(self, api_config, user_params, api_client, csr_generator):
        """
        :param api_config: Api settings
        :type api_config: ApiProductionConfig|ApiSandboxConfig

        :param user_params: User input
        :type user_params: dict

        :param api_client: Api client
        :type api_client: ApiClient

        :param csr_generator: csr generator
        :type csr_generator: CsrGenerator
        """
        self.api_config = api_config
        self.params = user_params
        self.api_client = api_client
        self.generator = csr_generator

    def execute(self, command):
        """
        Executes flow scenario, entry point for a class instance

        :param command: Command name to execute
        :type command: string
        :return: Api command response
        :rtype: ApiResponse
        """
        logger.info('Executing operation: [{}]'.format(command))
        api_response = self.call_method(command)
        if api_response.is_successful():
            logger.info('Operation [{}] was performed successfully.'.format(command))
            return api_response
        else:
            logger.error('API Error was encountered on [{}] operation.'.format(command))
            return api_response

    def create(self):
        create_params = self.api_config.get_create_params()
        create_params.update(self.params)
        return self.send_request(create_params)

    def activate(self):
        self.params['csr'] = self.generator.generate_csr(self.params['common_name'])
        del self.params['common_name']
        activate_params = self.api_config.get_activate_params()
        activate_params.update(self.params)
        return self.send_request(activate_params)

    def getinfo(self):
        getinfo_params = self.api_config.get_getinfo_params()
        getinfo_params.update(self.params)
        return self.send_request(getinfo_params)

    def create_and_activate(self):
        create_response = self.execute(FlowController.OPERATION_NAME_CREATE)
        self.params['CertificateID'] = create_response.get_certificate_id()
        return self.execute(FlowController.OPERATION_NAME_ACTIVATE)

    def retry_dcv(self):
        retry_dcv_params = self.api_config.get_retry_dcv_params()
        retry_dcv_params.update(self.params)
        return self.send_request(retry_dcv_params)

    def renew(self):
        renew_params = self.api_config.get_renew_params()
        renew_params.update(self.params)
        return self.send_request(renew_params)

    def revoke(self):
        revoke_params = self.api_config.get_revoke_params()
        revoke_params.update(self.params)
        return self.send_request(revoke_params)

    def reissue(self):
        self.params['csr'] = self.generator.generate_csr(self.params['common_name'])
        del self.params['common_name']
        reissue_params = self.api_config.get_reissue_params()
        reissue_params.update(self.params)
        return self.send_request(reissue_params)

    def getlist(self):
        getlist_params = self.api_config.get_getlist_params()
        getlist_params.update(self.params)
        return self.send_request(getlist_params)

    def get_email_list(self):
        get_email_list_params = self.api_config.get_email_list_params()
        get_email_list_params.update(self.params)
        return self.send_request(get_email_list_params)

    def call_method(self, method_name):
        return getattr(self, method_name)()

    def send_request(self, payload):
        return self.api_client.send_call(payload)
