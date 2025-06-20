from typing import Dict, Optional, TypeVar, List

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
    def get_clubs(cls, division_id: int, limit: int = 0, offset: int = 0) -> List[TMClub]:
        """
        Get all clubs in a specific division.
        :param division_id: The ID of the division.
        :param limit: The maximum number of clubs to return (0 for no limit).
        :param offset: The number of clubs to skip before starting to collect the result set.
        :return: A list of TMClub instances belonging to the specified division.
        """
        if not division_id:
            return []
        clubs = TMClub.objects.belong_to_division(division_id=division_id)
        if limit and offset:
            clubs = clubs[offset:offset + limit]
        return list(clubs)
