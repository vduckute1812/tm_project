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
