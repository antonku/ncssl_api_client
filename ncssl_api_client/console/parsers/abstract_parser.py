class AbstractParser:

    def add_parser(self, subparsers):
        self.parser = subparsers.add_parser(self.name, help=self.help)
        self.parser.add_argument("-sb", "--sandbox", help="Sandbox", action='store_true')