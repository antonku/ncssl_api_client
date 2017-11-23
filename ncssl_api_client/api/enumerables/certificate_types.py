from enum import Enum


class CertificateTypes(Enum):

    InstantSSL = 'InstantSSL'
    PositiveSSL = 'PositiveSSL'
    PositiveSSL_Wildcard = 'PositiveSSL Wildcard'
    EssentialSSL = 'EssentialSSL'
    EssentialSSL_Wildcard = 'EssentialSSL Wildcard'
    InstantSSL_Pro = 'InstantSSL Pro'
    PremiumSSL = 'PremiumSSL'
    PremiumSSL_Wildcard = 'PremiumSSL Wildcard'
    EV_SSL = 'EV SSL'
    EV_Multi_Domain_SSL = 'EV Multi Domain SSL'
    Multi_Domain_SSL = 'Multi Domain SSL'
    PositiveSSL_Multi_Domain = 'PositiveSSL Multi Domain'
    Unified_Communications = 'Unified Communications'

    def __str__(self):
        return self.value
