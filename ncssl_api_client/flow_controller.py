import logging

from ncssl_api_client.api.api_client import ApiClient
from ncssl_api_client.config.api.api_sandbox_config import ApiSandboxConfig
from ncssl_api_client.crypto.generator import CsrGenerator
from ncssl_api_client.api.api_response import ApiResponse

logger = logging.getLogger(__name__)


class FlowController:

    OPERATION_NAME_CREATE_AND_ACTIVATE = 'create_and_activate'
    OPERATION_NAME_ACTIVATE = 'activate'
    OPERATION_NAME_CREATE = 'create'
    OPERATION_NAME_GETINFO = 'getinfo'
    OPERATION_NAME_RETRY_DCV = 'retry_dcv'

    def __init__(self, api_config, crypto_config, user_params):
        """
        :param api_config: Api settings
        :type api_config: ApiProductionConfig|ApiSandboxConfig

        :param crypto_config: Crypto (key generation) settings
        :type crypto_config: CryptoConfig

        :param user_params: User input
        :type user_params: dict
        """
        self.api_config = api_config
        self.crypto_config = crypto_config
        self.params = user_params
        self.api_client = ApiClient(api_config)
        self.generator = CsrGenerator(crypto_config)

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
            logger.error('API Error was encountered on [{}] operation. *** ABORTING ***'.format(command))

    def create(self):
        create_params = self.api_config.get_create_params()
        create_params.update(self.params)
        return self.api_client.send_call(create_params)

    def activate(self):
        self.params['csr'] = self.generator.generate_csr(self.params['common_name'])
        del self.params['common_name']
        activate_params = self.api_config.get_activate_params()
        activate_params.update(self.params)
        return self.api_client.send_call(activate_params)

    def getinfo(self):
        getinfo_params = self.api_config.get_getinfo_params()
        getinfo_params.update(self.params)
        return self.api_client.send_call(getinfo_params)

    def create_and_activate(self):
        create_response = self.execute(FlowController.OPERATION_NAME_CREATE)
        self.params['CertificateID'] = create_response.get_certificate_id()
        return self.execute(FlowController.OPERATION_NAME_ACTIVATE)

    def retry_dcv(self):
        retry_dcv_params = self.api_config.get_retry_dcv_params()
        retry_dcv_params.update(self.params)
        return self.api_client.send_call(retry_dcv_params)

    def renew(self):
        raise NotImplementedError

    def reissue(self):
        raise NotImplementedError

    def call_method(self, method_name):
        return getattr(self, method_name)()
