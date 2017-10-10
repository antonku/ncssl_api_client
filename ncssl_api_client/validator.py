from ncssl_api_client.api.enumerables.filters import Filters
from ncssl_api_client.api.enumerables.sorters import Sorters
from ncssl_api_client.api.enumerables.certificate_types import CertificateTypes


class Validator:

    @staticmethod
    def validate_filter(filter_input):
        valid_values = [filter_opt.value for filter_opt in Filters]
        valid_filter = Validator.validate_enum_value(valid_values, filter_input)
        if len(valid_filter):
            return valid_filter.pop()
        raise ValueError('Invalid filter option, available options are %s' % valid_values)

    @staticmethod
    def validate_sorter(sorter_input):
        valid_values = [sorter_opt.value for sorter_opt in Sorters]
        valid_sorter = Validator.validate_enum_value(valid_values, sorter_input)
        if len(valid_sorter):
            return valid_sorter.pop()
        raise ValueError('Invalid sorting option, available options are %s' % valid_values)

    @staticmethod
    def validate_certificate_type(type_input):
        valid_values = [cert_type.value for cert_type in CertificateTypes]
        valid_type = Validator.validate_enum_value(valid_values, type_input)
        if len(valid_type):
            return valid_type.pop()
        raise ValueError('Invalid certificate type, supported types are %s' % valid_values)

    @staticmethod
    def validate_enum_value(enum, input_value):
        return list(filter(
            lambda valid_value: input_value.lower() == valid_value.lower(), enum
        ))
