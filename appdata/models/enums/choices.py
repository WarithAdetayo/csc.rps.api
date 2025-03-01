from commons.utils.enum import Enum


class Gender(Enum):
    MALE = 'MALE'
    FEMALE = 'FEMALE'


class ModeOfEntry(Enum):
    DE = 'DE'
    UTME = 'UTME'
    TRANSFER = 'TRANSFER'


class ParseStatus(Enum):
    PENDING = 'PENDING'
    FAILED = 'FAILED'
    SUCCESSFUL = 'SUCCESSFUL'
