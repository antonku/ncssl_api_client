import argparse
import sys
from ncssl_api_client.api.commands.invoker import Invoker
from ncssl_api_client.console.parsers.create_parser import CreateParser
from ncssl_api_client.console.parsers.activate_parser import ActivateParser
from ncssl_api_client.console.parsers.get_email_list_parser import GetEmailListParser
from ncssl_api_client.console.parsers.get_list_parser import GetListParser
from ncssl_api_client.console.parsers.getinfo_parser import GetInfoParser
from ncssl_api_client.console.parsers.reissue_parser import ReissueParser
from ncssl_api_client.console.parsers.renew_parser import RenewParser
from ncssl_api_client.console.parsers.retry_dcv_parser import RetryDcvParser
from ncssl_api_client.console.parsers.revoke_parser import RevokeParser


def get_args(args):
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(help='Available commands:', dest='command')
    CreateParser().add_parser(subparsers)
    ActivateParser().add_parser(subparsers)
    GetEmailListParser().add_parser(subparsers)
    GetListParser().add_parser(subparsers)
    GetInfoParser().add_parser(subparsers)
    ReissueParser().add_parser(subparsers)
    RenewParser().add_parser(subparsers)
    RetryDcvParser().add_parser(subparsers)
    RevokeParser().add_parser(subparsers)

    return parser.parse_args(args)


def main():
    arguments = get_args(sys.argv[1:])
    invoker = Invoker(arguments)
    return invoker.run()


def main_cli_wrapper():
    result = main()
    if result.is_successful():
        exit(0)
    else:
        exit(1)
