from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    first_name: str
    last_name: str
    email: EmailStr
    token: str = None
    token_expired: datetime = None
