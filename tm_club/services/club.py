from typing import Dict, Optional, TypeVar

from tm_club.models import TMClub
from tm_utils.services.utils.function import save_data, safe_executor


class ClubService:
    @classmethod
    @safe_executor(with_log=True, default=None)
    def get(cls, pk: int) -> Optional[TMClub]:
        """
        Get the toastmaster club instance by its primary key.
        :param pk:
        :return: the TMClub instance if found, otherwise None
        """
        return TMClub.objects.get(pk=pk)

