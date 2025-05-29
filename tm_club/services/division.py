from typing import Dict, Optional

from tm_club.models import TMDivision
from tm_utils.services.utils.function import save_data, safe_executor


class DivisionService:
    @classmethod
    @safe_executor(with_log=True, default=None)
    def get(cls, pk: int) -> Optional[TMDivision]:
        """
        Get the toastmaster division instance by its primary key.
        :param pk:
        :return: the TMDivision instance if found, otherwise None
        """
        return TMDivision.objects.get(pk=pk)

    @classmethod
    @safe_executor(with_transaction=True)
    def save(cls, data: Dict, instance: Optional[TMDivision] = None) -> TMDivision:
        """
        Save the toastmaster division instance with the provided data.
        If an instance is provided, update it; otherwise, create a new one.
        :param data: provided data to update or create the instance
        :param instance: optional instance to update
        :return: the saved TMDivision instance
        """
        return save_data(TMDivision, data, instance)
