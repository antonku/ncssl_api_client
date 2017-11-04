from ncssl_api_client.api.commands.abstract_command import AbstractCommand
from ncssl_api_client.crypto.csr_generator import CsrGenerator
from ncssl_api_client.config.manager import ConfigManager


class ActivateCommand(AbstractCommand):

    def __init__(self, command_config, api_client):
        super(ActivateCommand, self).__init__(command_config, api_client)
        self.command_config['csr'] = self.get_csr()

    def get_csr(self):
        crypto_config = self.get_crypto_config()
        csr_generator = CsrGenerator(crypto_config)
        csr = csr_generator.generate_csr(self.command_config['common_name'])
        del self.command_config['common_name']
        return csr

    def get_crypto_config(self):
        crypto_config = ConfigManager.get_crypto_config()
        if getattr(self.command_config, 'encrypt', False) is True:
            crypto_config.enable_key_encryption()
        return crypto_config
