from datetime import datetime, timedelta

from app.repositories.fake_user_repository import FakeUserRepository
from app.utils.token_generator import TokenGenerator


class UserController:

    def __init__(self):
        self.repository = FakeUserRepository()
        self.token_generator = TokenGenerator()

    def authenticate(self, username: str, password: str):
        user = self.repository.get_by_username(username)

        if not user:
            return False

        if password != user.password:
            return False

        user.token_expired = datetime.now() + timedelta(hours=6)
        user.token = self.token_generator.generate_token(user.username, user.token_expired)
        self.repository.update(user)
        return user
