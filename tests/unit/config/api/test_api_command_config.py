import mock
from unittest import TestCase
from ncssl_api_client.config.api.api_command_config import ApiCommandConfig


@mock.patch('ncssl_api_client.config.api.api_command_config.settings')
class ApiCommandConfigTest(TestCase):

    command_config_mock = {
        'activate': 'ACTIVATE TEST',
        'create': 'CREATE TEST',
        'get_email_list': 'GET EMAIL LIST TEST',
        'getinfo': 'GET INFO TEST',
        'getlist': 'GET LIST TEST',
        'reissue': 'REISSUE TEST',
        'renew': 'RENEW TEST',
        'retry_dcv': 'RETRY DCV TEST',
        'revoke': 'REVOKE TEST',
    }

    def test_ReturnsCreateConfig(self, settings_mock):
        settings_mock.command = self.command_config_mock
        api_command_config = ApiCommandConfig()
        command_params = api_command_config.get_create_params()
        self.assertEqual(command_params, 'CREATE TEST')

    def test_ReturnsActivateConfig(self, settings_mock):
        settings_mock.command = self.command_config_mock
        api_command_config = ApiCommandConfig()
        command_params = api_command_config.get_activate_params()
        self.assertEqual(command_params, 'ACTIVATE TEST')
        
    def test_ReturnsReissueConfig(self, settings_mock):
        settings_mock.command = self.command_config_mock
        api_command_config = ApiCommandConfig()
        command_params = api_command_config.get_reissue_params()
        self.assertEqual(command_params, 'REISSUE TEST')
        
    def test_ReturnsGetInfoConfig(self, settings_mock):
        settings_mock.command = self.command_config_mock
        api_command_config = ApiCommandConfig()
        command_params = api_command_config.get_getinfo_params()
        self.assertEqual(command_params, 'GET INFO TEST')

    def test_ReturnsRetryDcvConfig(self, settings_mock):
        settings_mock.command = self.command_config_mock
        api_command_config = ApiCommandConfig()
        command_params = api_command_config.get_retry_dcv_params()
        self.assertEqual(command_params, 'RETRY DCV TEST')

    def test_ReturnsRenewConfig(self, settings_mock):
        settings_mock.command = self.command_config_mock
        api_command_config = ApiCommandConfig()
        command_params = api_command_config.get_renew_params()
        self.assertEqual(command_params, 'RENEW TEST')

    def test_ReturnsRevokeConfig(self, settings_mock):
        settings_mock.command = self.command_config_mock
        api_command_config = ApiCommandConfig()
        command_params = api_command_config.get_revoke_params()
        self.assertEqual(command_params, 'REVOKE TEST')

    def test_ReturnsGetListConfig(self, settings_mock):
        settings_mock.command = self.command_config_mock
        api_command_config = ApiCommandConfig()
        command_params = api_command_config.get_getlist_params()
        self.assertEqual(command_params, 'GET LIST TEST')

    def test_ReturnsGetEmailListConfig(self, settings_mock):
        settings_mock.command = self.command_config_mock
        api_command_config = ApiCommandConfig()
        command_params = api_command_config.get_email_list_params()
        self.assertEqual(command_params, 'GET EMAIL LIST TEST')

