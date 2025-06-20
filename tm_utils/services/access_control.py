from toastmaster import tm_local
from typing import Optional

class AccessControlManager:
    @classmethod
    def get_local_access_control(cls) -> Optional[dict]:
        """
        Get the local access control for the given request.
        """
        return getattr(tm_local, "access_control", None)
    
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
