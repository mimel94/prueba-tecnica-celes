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

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "first_name": "Miller",
                "last_name": "Garcia",
                "email": "miller.garcia@example.com",
                "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMTIzZTQ1NjctZTg5Yi0xMmQzLWE0NTYtNDI2NjE0MTc0MDAwIiwidXNlcm5hbWUiOiJKb2huIERvZSIsImV4cCI6MTYwOTU2Nzg2NH0.0PO5BZnMj6Yp6Y3OjR3PC1H_AbO4BZyTSGTHF4G_YEE",
                "token_expired": "2023-01-01T00:00:00"
            }
        }


