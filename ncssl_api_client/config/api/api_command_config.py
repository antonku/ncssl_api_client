from ncssl_api_client.config.api import settings


class ApiCommandConfig:
    def __init__(self):
        self.create_params = settings.command['create']
        self.activate_params = settings.command['activate']
        self.reissue_params = settings.command['reissue']
        self.getinfo_params = settings.command['getinfo']
        self.retry_dcv_params = settings.command['retry_dcv']
        self.renew_params = settings.command['renew']
        self.revoke_params = settings.command['revoke']
        self.getlist_params = settings.command['getlist']
        self.getemaillist_params = settings.command['get_email_list']

    def get_create_params(self):
        return self.create_params

    def get_activate_params(self):
        return self.activate_params

    def get_reissue_params(self):
        return self.reissue_params

    def get_getinfo_params(self):
        return self.getinfo_params

    def get_retry_dcv_params(self):
        return self.retry_dcv_params

    def get_renew_params(self):
        return self.renew_params

    def get_revoke_params(self):
        return self.revoke_params

    def get_getlist_params(self):
        return self.getlist_params

    def get_email_list_params(self):
        return self.getemaillist_params

