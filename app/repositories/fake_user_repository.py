from typing import Optional, List

from app.models.user import User
from app.repositories.user_repository import UserRepository


class FakeUserRepository(UserRepository):

    def __init__(self):
        self.users: List[User] = []

    def create(self, user: User) -> None:
        self.users.append(user)

    def get_by_username(self, username: str) -> Optional[User]:
        for user in self.users:
            if user.username == username:
                return user
        return None

    def update(self, user: User) -> None:
        for _user in self.users:
            if _user.id == user.id:
                self.users.remove(user)
        self.users.append(user)
