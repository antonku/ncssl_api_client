from abc import ABCMeta
from future.utils import with_metaclass


class AbstractCommand(with_metaclass(ABCMeta)):

    def __init__(self, command_config, api_client):
        self.command_config = command_config
        self.api_client = api_client

    def execute(self):
        return self.api_client.send_call(self.command_config)
