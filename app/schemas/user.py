from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class User(BaseModel):
    email: str


class UserInDB(User):
    hashed_password: str


class UserCredentials(BaseModel):
    email: str
    password: str
