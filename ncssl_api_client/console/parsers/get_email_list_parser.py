from ncssl_api_client.console.parsers.abstract_parser import AbstractParser
from ncssl_api_client.api.commands.invoker import Invoker


class GetEmailListParser(AbstractParser):

    def __init__(self):
        self.name = Invoker.COMMAND_NAME_GET_EMAIL_LIST
        self.help = "Shows list of possible approval emails for a domain"

    def add_parser(self, subparsers):
        super(GetEmailListParser, self).add_parser(subparsers)
        self.parser.add_argument("-t", "--type", help="Certificate type", type=str, dest='CertificateType', required=True)
        self.parser.add_argument("-d", "--domain", help="Domain name", type=str, dest='DomainName', required=True)