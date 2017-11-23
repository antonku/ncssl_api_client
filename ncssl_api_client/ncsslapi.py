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

    args = parser.parse_args(args)

    # validation
    # TODO: move it elsewhere
    # TODO: move this file into console dir
    if args.command == 'activate':
        if (not getattr(args, 'CertificateID', False)) and (not (getattr(args, 'new', False))):
            parser.error('You must either specify certificate id or "-new" prefix for activate operation')

    if (args.command == 'activate') or (args.command == 'reissue'):
        if (not args.HTTPDCValidation) and (not args.DNSDCValidation) and (not (getattr(args, 'ApproverEmail', False))):
            parser.error('You must specify either "http_dcv", "cname_dcv" or approver email address')
    
    return args


def main():

    arguments = get_args(sys.argv[1:])
    invoker = Invoker(arguments)
    return invoker.run()

