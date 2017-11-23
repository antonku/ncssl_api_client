from ncssl_api_client.console.parsers.abstract_parser import AbstractParser
from ncssl_api_client.api.commands.invoker import Invoker
from ncssl_api_client.api.enumerables.filters import Filters
from ncssl_api_client.api.enumerables.sorters import Sorters


class GetListParser(AbstractParser):

    def __init__(self):
        self.name = Invoker.COMMAND_NAME_GET_LIST
        self.help = "Shows list of SSL certificates in your account"

    def add_parser(self, subparsers):
        super(GetListParser, self).add_parser(subparsers)
        self.parser.add_argument("-kw", "--keyword", help="Key word", type=str, dest='SearchTerm')
        self.parser.add_argument("-f", "--filter", help="Filter", type=Filters, dest='ListType', choices=list(Filters))
        self.parser.add_argument("-s", "--sort_by", help="Sort by", type=Sorters, dest='SortBy', choices=list(Sorters))