from enum import Enum

class Level(Enum):
    UNKNOWN = 0
    ICE_BREAKER = 1
    LEVEL_1_1 = 2
    LEVEL_1_2 = 3
    LEVEL_1_3 = 4
    LEVEL_1_4 = 5
    LEVEL_2_1 = 6
    LEVEL_2_2 = 7
    LEVEL_2_3 = 8
    LEVEL_3_1 = 9
    LEVEL_3_2 = 10
    LEVEL_3_3 = 11
    LEVEL_4_1 = 12
    LEVEL_4_2 = 13
    LEVEL_5_1 = 14
    LEVEL_5_2 = 15

    @classmethod
    def label(cls, value: int) -> str:
        return {
            cls.ICE_BREAKER: "Ice Breaker",
            cls.LEVEL_1_1: "Level 1.1",
            cls.LEVEL_1_2: "Level 1.2",
            cls.LEVEL_1_3: "Level 1.3",
            cls.LEVEL_1_4: "Level 1.4",
            cls.LEVEL_2_1: "Level 2.1",
            cls.LEVEL_2_2: "Level 2.2",
            cls.LEVEL_2_3: "Level 2.3",
            cls.LEVEL_3_1: "Level 3.1",
            cls.LEVEL_3_2: "Level 3.2",
            cls.LEVEL_3_3: "Level 3.3",
            cls.LEVEL_4_1: "Level 4.1",
            cls.LEVEL_4_2: "Level 4.2",
            cls.LEVEL_5_1: "Level 5.1",
            cls.LEVEL_5_2: "Level 5.2",
        }.get(value, "Unknown")


class VerificationType:
    NEW_GUEST = 1   # For new Guest, we send verification code to Guest after they register
    TOASTMASTER = 2 # We send verification code to Guest after they paid for Toastmaster membership
