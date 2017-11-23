from enum import Enum


class Sorters(Enum):

    PURCHASEDATE = 'PURCHASEDATE'
    PURCHASEDATE_DESC = 'PURCHASEDATE_DESC'
    SSLTYPE = 'SSLTYPE'
    SSLTYPE_DESC = 'SSLTYPE_DESC'
    EXPIREDATETIME = 'EXPIREDATETIME'
    EXPIREDATETIME_DESC = 'EXPIREDATETIME_DESC'
    HOST_NAME = 'Host_Name'
    HOST_NAME_DESC = 'Host_Name_DESC'

    def __str__(self):
        return self.value
