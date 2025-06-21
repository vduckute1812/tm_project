from tm_utils.exceptions.tm_club import ClubNotFound
from toastmaster.settings import tm_local
from typing import Optional

class AccessControlService:
    @classmethod
    def get_club_id(cls, request=None, raise_exception=True) -> Optional[str]:
        """
        Get the club ID from the local access control for the given request.
        """
        club_id = 0
        request = request or AccessControlManager.get_request()
        if request:
            club_id = getattr(request, "club_id", None) or AccessControlManager.get_property("club_id")
        if not club_id and raise_exception:
            raise ClubNotFound()
        return club_id
    
    @classmethod
    def set_club_id(cls, request, club_id: int) -> None:
        """
        Set the club ID in the local access control for the given request.
        """
        if request:
            request.club_id = club_id
        AccessControlManager.set_property("club_id", str(club_id))


class AccessControlManager:
    @classmethod
    def get_local_access_control(cls) -> Optional[dict]:
        """
        Get the local access control for the given request.
        """
        return getattr(tm_local, "access_control", None)
    
    @classmethod
    def get_request(cls):
        """
        Get the local access control for the given request.
        """
        return getattr(tm_local, "request", None)
    
    @classmethod
    def set_property(cls, key: str, value: str) -> None:
        """
        Set the local access control for the given request.
        """
        access_control = cls.get_local_access_control()
        if isinstance(access_control, dict):
            tm_local.access_control[key] = value

    @classmethod
    def get_property(cls, key: str) -> Optional[str]:
        """
        Get the local access control for the given request.
        """
        access_control = cls.get_local_access_control()
        return access_control.get(key) if isinstance(access_control, dict) else None
