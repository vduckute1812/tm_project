from typing import Optional, Dict

from authtools.models import User

from tm_utils.services.utils.function import safe_executor, save_data


class UserService:
    @classmethod
    @safe_executor(with_transaction=True)
    def save(cls, data: Dict, instance: Optional[User]) -> User:
        """
        Save the toastmaster club instance with the provided data.
        If an instance is provided, update it; otherwise, create a new one.
        :param data: provided data to update or create the instance
        :param instance: optional instance to update
        :return: the saved TMClub instance
        """
        return save_data(User, data, instance)
