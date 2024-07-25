from app.schemas.user import UserInDB
from settings.base import pwd_context


class UserController:

    @staticmethod
    def get(db, username: str):
        if username in db:
            user_dict = db[username]
            return UserInDB(**user_dict)

    @classmethod
    def authenticate(cls, db, username: str, password: str):
        user = cls.get(db, username)
        if not user:
            return False
        if not pwd_context.verify(password, user.hashed_password):
            return False
        return user
