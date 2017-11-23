from ncssl_api_client.console.parsers.abstract_parser import AbstractParser
from ncssl_api_client.api.commands.invoker import Invoker
from ncssl_api_client.api.enumerables.certificate_types import CertificateTypes


class CreateParser(AbstractParser):

    def __init__(self):
        self.name = Invoker.COMMAND_NAME_CREATE
        self.help = 'Purchases a certificate'

    def add_parser(self, subparsers):
        super(CreateParser, self).add_parser(subparsers)
        self.parser.add_argument("-t", "--type", help="Type", type=CertificateTypes, default='PositiveSSL', dest='Type', choices=list(CertificateTypes))
        self.parser.add_argument("-y", "--years", help="Validity period", type=int, default=1, dest='Years')

