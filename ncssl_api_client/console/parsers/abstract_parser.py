from abc import ABCMeta
from future.utils import with_metaclass


class AbstractParser(with_metaclass(ABCMeta)):

    def add_parser(self, subparsers):
        self.parser = subparsers.add_parser(self.name, help=self.help)
        self.parser.add_argument("-sb", "--sandbox", help="Sandbox", action='store_true')
        self.parser.add_argument("-json", "--json", help="Return as json", action='store_true')