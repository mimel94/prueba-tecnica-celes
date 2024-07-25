from abc import ABC, abstractmethod
from typing import Optional

from app.models.user import User


class UserRepository(ABC):

    @abstractmethod
    def create(self, user: User) -> None:
        pass

    @abstractmethod
    def get_by_username(self, username: str) -> Optional[User]:
        pass

    @abstractmethod
    def update(self, user: User) -> None:
        pass
