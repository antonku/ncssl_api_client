from enum import Enum


class Filters(Enum):

    ALL = 'ALL'
    PROCESSING = 'Processing'
    EMAIL_SENT = 'EmailSent'
    TECHNICAL_PROBLEM = 'TechnicalProblem'
    IN_PROGRESS = 'InProgress'
    COMPLETED = 'Completed'
    DEACTIVATED = 'Deactivated'
    ACTIVE = 'Active'
    CANCELLED = 'Cancelled'
    NEWPURCHASE = 'NewPurchase'
    NEWRENEWAL = 'NewRenewal'

    def __str__(self):
        return self.value
