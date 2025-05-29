from enum import Enum


class PermissionType(Enum):
    NO_ACCESS = 1
    VIEW_ONLY = 2
    FULL_ACCESS = 3

class PermissionFeature(Enum):
    pass