from ncssl_api_client.console.parsers.abstract_parser import AbstractParser
from ncssl_api_client.api.commands.invoker import Invoker


class RetryDcvParser(AbstractParser):

    def __init__(self):
        self.name = Invoker.COMMAND_NAME_RETRY_DCV
        self.help = "Triggers domain control validation"

    def add_parser(self, subparsers):
        super(RetryDcvParser, self).add_parser(subparsers)
        self.parser.add_argument("-id", "--cert_id", help="Certificate ID to get info for", dest='CertificateID', required=True)