from abc import ABC, abstractmethod
from datetime import datetime

import jwt

from settings.base import SECRET_KEY


class TokenGenerator:

    @staticmethod
    def generate_token(username: str, token_expired: datetime):
        payload = {
            'username': username,
            'exp': token_expired.timestamp()
        }
        return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

    @staticmethod
    def decode_token(token: str) -> dict:
        try:
            return jwt.decode(token,SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError as e:
            raise jwt.ExpiredSignatureError(e)
        except jwt.InvalidTokenError as e:
            raise jwt.InvalidTokenError(e)
