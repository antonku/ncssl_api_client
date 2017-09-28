import argparse

from ncssl_api_client.config.manager import ConfigManager
from ncssl_api_client.flow_controller import FlowController
from ncssl_api_client.api.api_client import ApiClient
from ncssl_api_client.crypto.generator import CsrGenerator


def get_args():
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(help='sub-command help', dest='command')

    # create
    subparser_create = subparsers.add_parser(FlowController.OPERATION_NAME_CREATE)
    subparser_create.add_argument("-t", "--type", help="Type", type=str, default='PositiveSSL', dest='Type')
    subparser_create.add_argument("-sb", "--sandbox", help="Sandbox", action='store_true')

    # activate
    subparser_activate = subparsers.add_parser(FlowController.OPERATION_NAME_ACTIVATE)
    subparser_activate.add_argument("-cn", "--common_name", help="Common Name", type=str, required=True)
    subparser_activate.add_argument("-sb", "--sandbox", help="Sandbox", action='store_true')
    subparser_activate.add_argument("-enc", "--encrypt", help="Whether to encrypt private key", action='store_true')
    subparser_activate.add_argument("-email", "--approver_email", help="Approver Email", type=str, dest='ApproverEmail')
    subparser_activate.add_argument("-new", "--new", help="Purchase new cert before activation", action='store_true')
    subparser_activate.add_argument("-id", "--cert_id", help="Certificate ID to activate", dest='CertificateID')
    subparser_activate.add_argument("-http", "--http_dcv", help="Use HTTP validation", action='store_true', dest='HTTPDCValidation')
    subparser_activate.add_argument("-cname", "--cname_dcv", help="Use DNS validation", action='store_true', dest='DNSDCValidation')

    # reissue
    subparser_reissue = subparsers.add_parser(FlowController.OPERATION_NAME_REISSUE)
    subparser_reissue.add_argument("-cn", "--common_name", help="Common Name", type=str, required=True)
    subparser_reissue.add_argument("-sb", "--sandbox", help="Sandbox", action='store_true')
    subparser_reissue.add_argument("-enc", "--encrypt", help="Whether to encrypt private key", action='store_true')
    subparser_reissue.add_argument("-email", "--approver_email", help="Approver Email", type=str, dest='ApproverEmail')
    subparser_reissue.add_argument("-id", "--cert_id", help="Certificate ID to activate", dest='CertificateID', required=True)
    subparser_reissue.add_argument("-http", "--http_dcv", help="Use HTTP validation", action='store_true', dest='HTTPDCValidation')
    subparser_reissue.add_argument("-cname", "--cname_dcv", help="Use DNS validation", action='store_true', dest='DNSDCValidation')

    # getinfo
    subparser_getinfo = subparsers.add_parser(FlowController.OPERATION_NAME_GETINFO)
    subparser_getinfo.add_argument("-id", "--cert_id", help="Certificate ID to get info for", dest='CertificateID', required=True)
    subparser_getinfo.add_argument("-sb", "--sandbox", help="Sandbox", action='store_true')

    # retry dcv
    subparser_getinfo = subparsers.add_parser(FlowController.OPERATION_NAME_RETRY_DCV)
    subparser_getinfo.add_argument("-id", "--cert_id", help="Certificate ID to get info for", dest='CertificateID', required=True)
    subparser_getinfo.add_argument("-sb", "--sandbox", help="Sandbox", action='store_true')

    # renew
    subparser_renew = subparsers.add_parser(FlowController.OPERATION_NAME_RENEW)
    subparser_renew.add_argument("-id", "--cert_id", help="Certificate ID to get info for", dest='CertificateID', required=True)
    subparser_renew.add_argument("-t", "--type", help="Type", type=str, default='PositiveSSL', dest='SSLType', required=True)
    subparser_renew.add_argument("-y", "--years", help="Validity period", type=int, default=1, dest='Years')
    subparser_renew.add_argument("-sb", "--sandbox", help="Sandbox", action='store_true')

    # revoke
    subparser_revoke = subparsers.add_parser(FlowController.OPERATION_NAME_REVOKE)
    subparser_revoke.add_argument("-id", "--cert_id", help="Certificate ID to revoke", dest='CertificateID', required=True)
    subparser_revoke.add_argument("-t", "--type", help="Type", type=str, dest='CertificateType', required=True)
    subparser_revoke.add_argument("-sb", "--sandbox", help="Sandbox", action='store_true')

    # getlist
    subparser_getlist = subparsers.add_parser(FlowController.OPERATION_NAME_GET_LIST)
    subparser_getlist.add_argument("-sb", "--sandbox", help="Sandbox", action='store_true')
    subparser_getlist.add_argument("-kw", "--keyword", help="Key word", type=str, dest='SearchTerm')

    args = parser.parse_args()

    if args.command == 'activate':
        if (not getattr(args, 'CertificateID', False)) and (not (getattr(args, 'new', False))):
            parser.error('You must either specify certificate id or "-new" prefix for activate operation')

    if (args.command == 'activate') or (args.command == 'reissue'):
        if (not args.HTTPDCValidation) and (not args.DNSDCValidation) and (not (getattr(args, 'ApproverEmail', False))):
            parser.error('You must specify either "http_dcv", "cname_dcv" or approver email address')

    return args


if __name__ == '__main__':

    arguments = get_args()

    crypto_config = ConfigManager.get_crypto_config()
    if getattr(arguments, 'encrypt', False) is True:
        crypto_config.enable_key_encryption()

    if arguments.sandbox is True:
        api_config = ConfigManager.get_api_sandbox_config()
    else:
        api_config = ConfigManager.get_api_production_config()

    params = {k: v for (k, v) in vars(arguments).items() if k != 'command'}
    if (arguments.command == 'activate') and (arguments.new is True):
        command = FlowController.OPERATION_NAME_CREATE_AND_ACTIVATE
    else:
        command = arguments.command

    api_client = ApiClient(api_config)
    csr_generator = CsrGenerator(crypto_config)

    controller = FlowController(api_config, params, api_client, csr_generator)
    controller.execute(command)

