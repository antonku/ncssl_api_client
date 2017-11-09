from ncssl_api_client.console.parsers.abstract_parser import AbstractParser
from ncssl_api_client.api.commands.invoker import Invoker


class CreateParser(AbstractParser):

    def __init__(self):
        self.name = Invoker.COMMAND_NAME_CREATE
        self.help = 'Purchases a certificate'

    def add_parser(self, subparsers):
        super(CreateParser, self).add_parser(subparsers)
        self.parser.add_argument("-t", "--type", help="Type", type=str, default='PositiveSSL', dest='Type')
        self.parser.add_argument("-y", "--years", help="Validity period", type=int, default=1, dest='Years')

