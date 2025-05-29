from enum import Enum


class SessionType(Enum):
    UNKNOWN = 0
    TABLE_TOPIC = 1
    PREPARED_SPEECH = 2
    EVALUATION = 3

class MeetingRole(Enum):
    UNKNOWN = 0
    SERGENT_AT_ARM = 1
    MC = 2
    TABLE_TOPIC = 3
    PREPARED_SPEECH = 4
    EVALUATION = 5
    TIME_KEEPER = 6
    GRAMMARIAN = 7
    AH_COUNTER = 8
    GENERAL_EVALUATOR = 9
    PRESIDENT = 10
