import argparse
from ncssl_api_client.api.api_client import ApiClient
from ncssl_api_client.config.manager import ConfigManager
from ncssl_api_client.crypto.csr_generator import CsrGenerator
from ncssl_api_client.flow_controller import FlowController
from ncssl_api_client.validator import Validator


def get_args():
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(help='Available commands:', dest='command')

    # create
    subparser_create = subparsers.add_parser(FlowController.OPERATION_NAME_CREATE, help="Purchases a certificate")
    subparser_create.add_argument("-t", "--type", help="Type", type=str, default='PositiveSSL', dest='Type')
    subparser_create.add_argument("-y", "--years", help="Validity period", type=int, default=1, dest='Years')
    subparser_create.add_argument("-sb", "--sandbox", help="Sandbox", action='store_true')

    # activate
    subparser_activate = subparsers.add_parser(
        FlowController.OPERATION_NAME_ACTIVATE,
        help="Generates CSR and activates a certificate with it"
    )
    subparser_activate.add_argument("-cn", "--common_name", help="Common Name to activate certificate for", type=str, required=True)
    subparser_activate.add_argument("-sb", "--sandbox", help="Whether to use sandbox api", action='store_true')
    subparser_activate.add_argument("-enc", "--encrypt", help="Whether to encrypt private key", action='store_true')
    subparser_activate.add_argument("-e", "--email", help="Approver Email", type=str, dest='ApproverEmail')
    subparser_activate.add_argument("-new", "--new", help="Purchase new cert before activation", action='store_true')
    subparser_activate.add_argument("-id", "--cert_id", help="Certificate ID to activate", dest='CertificateID')
    subparser_activate.add_argument("-http", "--http_dcv", help="Use HTTP validation", action='store_true', dest='HTTPDCValidation')
    subparser_activate.add_argument("-dns", "--dns_dcv", help="Use DNS validation", action='store_true', dest='DNSDCValidation')
    subparser_activate.add_argument("-t", "--type", help="Certificate Type", type=str, default='PositiveSSL', dest='Type')
    subparser_activate.add_argument("-y", "--years", help="Validity period", type=int, default=1, dest='Years')

    # reissue
    subparser_reissue = subparsers.add_parser(
        FlowController.OPERATION_NAME_REISSUE,
        help='Generates CSR and reissues a certificate with it'
    )
    subparser_reissue.add_argument("-cn", "--common_name", help="Common Name", type=str, required=True)
    subparser_reissue.add_argument("-sb", "--sandbox", help="Sandbox", action='store_true')
    subparser_reissue.add_argument("-enc", "--encrypt", help="Whether to encrypt private key", action='store_true')
    subparser_reissue.add_argument("-e", "--email", help="Approver Email", type=str, dest='ApproverEmail')
    subparser_reissue.add_argument("-id", "--cert_id", help="Certificate ID to activate", dest='CertificateID', required=True)
    subparser_reissue.add_argument("-http", "--http_dcv", help="Use HTTP validation", action='store_true', dest='HTTPDCValidation')
    subparser_reissue.add_argument("-dns", "--dns_dcv", help="Use DNS validation", action='store_true', dest='DNSDCValidation')

    # getinfo
    subparser_getinfo = subparsers.add_parser(
        FlowController.OPERATION_NAME_GETINFO,
        help='Shows information for a particular certificate'
    )
    subparser_getinfo.add_argument("-id", "--cert_id", help="Certificate ID to get info for", dest='CertificateID', required=True)
    subparser_getinfo.add_argument("-sb", "--sandbox", help="Sandbox", action='store_true')
    subparser_getinfo.add_argument("-rc", "--return_certs", help="Return certificates in response", action='store_true', dest='ReturnCertificate')

    # retry dcv
    subparser_getinfo = subparsers.add_parser(
        FlowController.OPERATION_NAME_RETRY_DCV,
        help='Triggers domain control validation'
    )
    subparser_getinfo.add_argument("-id", "--cert_id", help="Certificate ID to get info for", dest='CertificateID', required=True)
    subparser_getinfo.add_argument("-sb", "--sandbox", help="Sandbox", action='store_true')

    # renew
    subparser_renew = subparsers.add_parser(
        FlowController.OPERATION_NAME_RENEW,
        help='Purchases a renewal certificate'
    )
    subparser_renew.add_argument("-id", "--cert_id", help="Certificate ID to get info for", dest='CertificateID', required=True)
    subparser_renew.add_argument("-t", "--type", help="Type", type=str, default='PositiveSSL', dest='SSLType', required=True)
    subparser_renew.add_argument("-y", "--years", help="Validity period", type=int, default=1, dest='Years')
    subparser_renew.add_argument("-sb", "--sandbox", help="Sandbox", action='store_true')

    # revoke
    subparser_revoke = subparsers.add_parser(
        FlowController.OPERATION_NAME_REVOKE,
        help='Revokes a certificate'
    )
    subparser_revoke.add_argument("-id", "--cert_id", help="Certificate ID to revoke", dest='CertificateID', required=True)
    subparser_revoke.add_argument("-t", "--type", help="Type", type=str, dest='CertificateType', required=True)
    subparser_revoke.add_argument("-sb", "--sandbox", help="Sandbox", action='store_true')

    # getlist
    subparser_getlist = subparsers.add_parser(
        FlowController.OPERATION_NAME_GET_LIST,
        help='Shows list of SSL certificates in your account'
    )
    subparser_getlist.add_argument("-sb", "--sandbox", help="Sandbox", action='store_true')
    subparser_getlist.add_argument("-kw", "--keyword", help="Key word", type=str, dest='SearchTerm')
    subparser_getlist.add_argument("-f", "--filter", help="Filter", type=str, dest='ListType')
    subparser_getlist.add_argument("-s", "--sort_by", help="Sort by", type=str, dest='SortBy')

    # get email list
    subparser_get_email_list = subparsers.add_parser(
        FlowController.OPERATION_NAME_GET_EMAIL_LIST,
        help='Shows list of possible approval emails for a domain'
    )
    subparser_get_email_list.add_argument("-sb", "--sandbox", help="Sandbox", action='store_true')
    subparser_get_email_list.add_argument("-t", "--type", help="Certificate type", type=str, dest='CertificateType', required=True)
    subparser_get_email_list.add_argument("-d", "--domain", help="Domain name", type=str, dest='DomainName', required=True)

    args = parser.parse_args()

    # validation
    if args.command == 'activate':
        if (not getattr(args, 'CertificateID', False)) and (not (getattr(args, 'new', False))):
            parser.error('You must either specify certificate id or "-new" prefix for activate operation')

    if (args.command == 'activate') or (args.command == 'reissue'):
        if (not args.HTTPDCValidation) and (not args.DNSDCValidation) and (not (getattr(args, 'ApproverEmail', False))):
            parser.error('You must specify either "http_dcv", "cname_dcv" or approver email address')

    try:
        sorter_type = getattr(args, 'SortBy', None)
        if sorter_type:
            args.SortBy = Validator.validate_sorter(sorter_type)

        filter_type = getattr(args, 'ListType', None)
        if filter_type:
            args.ListType = Validator.validate_filter(filter_type)

        certificate_type = getattr(args, 'Type', None) or getattr(args, 'CertificateType', None)
        if certificate_type:
            args.ListType = Validator.validate_certificate_type(certificate_type)
    except ValueError as e:
        parser.error(str(e))
    
    return args


def main():

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
