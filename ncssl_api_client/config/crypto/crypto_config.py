from ncssl_api_client.config.crypto import settings


class CryptoConfig:

    def __init__(self):
        self.csr_subject = settings.csr_subject
        self.key_size = settings.key_size
        self.key_encryption = False
        self.key_encryption_algorithm = settings.key_encryption_algorithm

    def get_csr_subject(self):
        return self.csr_subject

    def get_key_size(self):
        return self.key_size

    def enable_key_encryption(self):
        self.key_encryption = True

    def key_encryption_enabled(self):
        return self.key_encryption

    def get_key_encryption_algorithm(self):
        return self.key_encryption_algorithm
