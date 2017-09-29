from ncssl_api_client.api.enumerables.filters import Filters
from ncssl_api_client.api.enumerables.sorters import Sorters


class Validator:

    @staticmethod
    def validate_filter(filter_input):
        valid_filter = list(filter(
            lambda v_filter: filter_input.lower() == v_filter.lower(),
            Filters.__members__
        ))
        if len(valid_filter):
            return valid_filter.pop()

    @staticmethod
    def validate_sorter(sorter_input):
        valid_filter = list(filter(
            lambda v_filter: sorter_input.lower() == v_filter.lower(),
            Sorters.__members__
        ))
        if len(valid_filter):
            return valid_filter.pop()
