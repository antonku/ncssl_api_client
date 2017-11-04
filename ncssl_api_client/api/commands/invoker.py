from ncssl_api_client.api.commands.activate_command import ActivateCommand
from ncssl_api_client.api.commands.create_command import CreateCommand
from ncssl_api_client.api.commands.get_email_list_command import GetEmailListCommand
from ncssl_api_client.api.commands.get_info_command import GetInfoCommand
from ncssl_api_client.api.commands.getlist_command import GetListCommand
from ncssl_api_client.api.commands.reissue_command import ReissueCommand
from ncssl_api_client.api.commands.renew_command import RenewCommand
from ncssl_api_client.api.commands.revoke_command import RevokeCommand
from ncssl_api_client.api.commands.retry_dcv_command import RetryDcvCommand
from ncssl_api_client.config.manager import ConfigManager
from ncssl_api_client.api.api_client import ApiClient


class Invoker:

    COMMAND_NAME_CREATE_AND_ACTIVATE = 'create_and_activate'  # TODO: Implement!
    COMMAND_NAME_ACTIVATE = 'activate'
    COMMAND_NAME_CREATE = 'create'
    COMMAND_NAME_GETINFO = 'getinfo'
    COMMAND_NAME_RETRY_DCV = 'retry_dcv'
    COMMAND_NAME_REISSUE = 'reissue'
    COMMAND_NAME_RENEW = 'renew'
    COMMAND_NAME_REVOKE = 'revoke'
    COMMAND_NAME_GET_LIST = 'getlist'
    COMMAND_NAME_GET_EMAIL_LIST = 'get_email_list'

    command_map = {
        COMMAND_NAME_ACTIVATE: {'configMethod': 'get_activate_params', 'class': ActivateCommand},
        COMMAND_NAME_REISSUE: {'configMethod': 'get_reissue_params', 'class': ReissueCommand},
        COMMAND_NAME_CREATE: {'configMethod': 'get_create_params', 'class': CreateCommand},
        COMMAND_NAME_GETINFO: {'configMethod': 'get_getinfo_params', 'class': GetInfoCommand},
        COMMAND_NAME_RETRY_DCV: {'configMethod': 'get_retry_dcv_params', 'class': RetryDcvCommand},
        COMMAND_NAME_RENEW: {'configMethod': 'get_renew_params', 'class': RenewCommand},
        COMMAND_NAME_REVOKE: {'configMethod': 'get_revoke_params', 'class': RevokeCommand},
        COMMAND_NAME_GET_LIST: {'configMethod': 'get_getlist_params', 'class': GetListCommand},
        COMMAND_NAME_GET_EMAIL_LIST: {'configMethod': 'get_email_list_params', 'class': GetEmailListCommand},
    }

    def __init__(self, arguments):

        self.arguments = arguments
        self.command_name = arguments.command

    def run(self):
        command = self.get_command()
        return command.execute()

    def get_command(self):
        params = {k: v for (k, v) in vars(self.arguments).items() if k != 'command'}
        command_config = self.get_command_config(params)
        command_class = self.command_map[self.command_name]['class']
        api_client = self.get_api_client()
        return command_class(command_config, api_client)

    def get_command_config(self, params):
        api_command_config = ConfigManager.get_api_command_config()
        command_config = getattr(api_command_config, self.command_map[self.command_name]['configMethod'])()
        command_config.update(params)
        return command_config

    def get_api_client(self):

        if self.arguments.sandbox is True:
            api_client_config = ConfigManager.get_api_sandbox_client_config()
        else:
            api_client_config = ConfigManager.get_api_production_client_config()

        api_client = ApiClient(api_client_config)
        return api_client


