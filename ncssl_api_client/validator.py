from ncssl_api_client.api.enumerables.filters import Filters
from ncssl_api_client.api.enumerables.sorters import Sorters
from ncssl_api_client.api.enumerables.certificate_types import CertificateTypes


class Validator:

    @staticmethod
    def validate_filter(filter_input):
        valid_filter = list(filter(
            lambda v_filter: filter_input.lower() == v_filter.lower(),
            Filters.__members__
        ))
        if len(valid_filter):
            return valid_filter.pop()
        raise ValueError('Invalid filter option, available options are %s' %
                         [filter_opt.value for filter_opt in Filters])

    @staticmethod
    def validate_sorter(sorter_input):
        valid_sorter = list(filter(
            lambda v_filter: sorter_input.lower() == v_filter.lower(),
            Sorters.__members__
        ))
        if len(valid_sorter):
            return valid_sorter.pop()
        raise ValueError('Invalid sorting option, available options are %s' %
                         [sorter_opt.value for sorter_opt in Sorters])

    @staticmethod
    def validate_certificate_type(type_input):
        valid_type = list(filter(
            lambda v_type: type_input.lower() == v_type.lower(),
            CertificateTypes.__members__
        ))
        if len(valid_type):
            return valid_type.pop()
        raise ValueError('Invalid certificate type, supported types are %s' %
                         [cert_type.value for cert_type in CertificateTypes])

