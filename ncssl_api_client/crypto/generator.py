import subprocess

from ncssl_api_client.config.crypto.crypto_config import CryptoConfig
from ncssl_api_client.utils.utils import Utils


class CsrGenerator:

    def __init__(self, config):
        """
        CSR Generator constructor

        :param config: crypto config
        :type config: CryptoConfig
        """
        self.config = config

    def _generate_key(self, file_name):
        key_size = self.config.get_key_size()
        openssl_args = 'genrsa -out {}.key {}'.format(file_name, key_size).split()
        if self.config.key_encryption_enabled():
            openssl_args.insert(1, self.config.get_key_encryption_algorithm())
        self.openssl_exec(openssl_args)

    def _prepare_fs(self, file_name):
        Utils.update_path(file_name)

    def _prepare_subject(self, common_name):
        subject = self.config.get_csr_subject()
        subject['CN'] = common_name
        return '/{}'.format('/'.join(['{}={}'.format(key, value) for key, value in subject.items()]))

    def generate_csr(self, common_name):

        # Prepare file system
        file_name = Utils.normalize_cn(common_name)
        self._prepare_fs(common_name)

        # generate private key
        self._generate_key(file_name)

        openssl_args = 'req -new -key {0}.key -out {0}.csr -subj'.format(file_name).split()
        openssl_args.append(self._prepare_subject(common_name))
        self.openssl_exec(openssl_args)

        return self.read_csr(file_name)

    @staticmethod
    def openssl_exec(cli_args):
        cli_args.insert(0, 'openssl')
        subprocess.run(cli_args)

    @staticmethod
    def read_csr(file_name):
        with open('{}.csr'.format(file_name)) as f:
            csr = f.read()
            f.close()
        return csr
