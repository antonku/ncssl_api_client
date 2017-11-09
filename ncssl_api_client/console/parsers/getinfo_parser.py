from ncssl_api_client.console.parsers.abstract_parser import AbstractParser
from ncssl_api_client.api.commands.invoker import Invoker


class GetInfoParser(AbstractParser):

    def __init__(self):
        self.name = Invoker.COMMAND_NAME_GETINFO
        self.help = "Shows information for a particular certificate"

    def add_parser(self, subparsers):
        super(GetInfoParser, self).add_parser(subparsers)
        self.parser.add_argument("-id", "--cert_id", help="Certificate ID to get info for", dest='CertificateID', required=True)
        self.parser.add_argument("-rc", "--return_certs", help="Return certificates in response", action='store_true', dest='ReturnCertificate')