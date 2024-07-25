import jwt
from fastapi import Header, HTTPException

from app.repositories.fake_user_repository import FakeUserRepository
from app.utils.token_generator import TokenGenerator


async def login_required(authorization: str = Header()):
    jwt_token = authorization.split(" ", 1)[1]
    try:
        token_decoded: dict = TokenGenerator.decode_token(token=jwt_token)
        user = FakeUserRepository().get_by_username(token_decoded['username'])
        if not user:
            raise HTTPException(status_code=401, detail="Unauthorized token")
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        raise HTTPException(status_code=401, detail="Unauthorized token")

