from ncssl_api_client.console.parsers.abstract_parser import AbstractParser
from ncssl_api_client.api.commands.invoker import Invoker
from ncssl_api_client.api.enumerables.certificate_types import CertificateTypes


class ReissueParser(AbstractParser):

    def __init__(self):
        self.name = Invoker.COMMAND_NAME_REISSUE
        self.help = "Generates CSR and reissues a certificate with it"

    def add_parser(self, subparsers):
        super(ReissueParser, self).add_parser(subparsers)
        self.parser.add_argument("-cn", "--common_name", help="Common Name to activate certificate for", type=str, required=True)
        self.parser.add_argument("-enc", "--encrypt", help="Whether to encrypt private key", action='store_true')
        self.parser.add_argument("-id", "--cert_id", help="Certificate ID to activate", dest='CertificateID')
        self.parser.add_argument("-t", "--type", help="Certificate Type", type=CertificateTypes, default='PositiveSSL', dest='Type', choices=list(CertificateTypes))
        self.parser.add_argument("-y", "--years", help="Validity period", type=int, default=1, dest='Years')
        group = self.parser.add_mutually_exclusive_group()
        group.add_argument("-http", "--http_dcv", help="Use HTTP validation", action='store_true', dest='HTTPDCValidation')
        group.add_argument("-dns", "--dns_dcv", help="Use DNS validation", action='store_true', dest='DNSDCValidation')
        group.add_argument("-e", "--email", help="Approver Email", type=str, dest='ApproverEmail')

