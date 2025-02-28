from commons.utils.enum import Enum


class RecommendedAction(Enum):
    DELETE = 'DELETE'
    UPDATE = 'UPDATE'


class ActionRecord(Enum):
    ACCEPTANCE_LETTER = 'ACCEPTANCE_LETTER'
    PLACEMENT_REQUEST = 'PLACEMENT_REQUEST'
    PLACEMENT = 'PLACEMENT'
