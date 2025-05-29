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

    @classmethod
    @safe_executor(with_transaction=True)
    def save(cls, data: Dict, instance: Optional[TMClub]) -> TMClub:
        """
        Save the toastmaster club instance with the provided data.
        If an instance is provided, update it; otherwise, create a new one.
        :param data: provided data to update or create the instance
        :param instance: optional instance to update
        :return: the saved TMClub instance
        """
        return save_data(TMClub, data, instance)

