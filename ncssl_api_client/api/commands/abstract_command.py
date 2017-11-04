from abc import ABCMeta


class AbstractCommand(metaclass=ABCMeta):

    def __init__(self, command_config, api_client):
        self.command_config = command_config
        self.api_client = api_client

    def execute(self):
        return self.api_client.send_call(self.command_config)
