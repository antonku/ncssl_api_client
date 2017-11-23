from ncssl_api_client.console.parsers.abstract_parser import AbstractParser
from ncssl_api_client.api.commands.invoker import Invoker
from ncssl_api_client.api.enumerables.certificate_types import CertificateTypes


class RevokeParser(AbstractParser):

    def __init__(self):
        self.name = Invoker.COMMAND_NAME_REVOKE
        self.help = "Revokes a certificate"

    def add_parser(self, subparsers):
        super(RevokeParser, self).add_parser(subparsers)
        self.parser.add_argument("-id", "--cert_id", help="Certificate ID to revoke", dest='CertificateID', required=True)
        self.parser.add_argument("-t", "--type", help="Type", type=CertificateTypes, dest='CertificateType', required=True, choices=list(CertificateTypes))