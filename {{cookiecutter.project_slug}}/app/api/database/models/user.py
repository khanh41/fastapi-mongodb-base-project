# pylint: skip-file
"""User Model."""
from datetime import datetime
from typing import Optional

from pydantic import Field

from app.api.database.models.base import CustomBaseModel


class UserSchema(CustomBaseModel):
    """User Schema."""
    user_id: Optional[str] = None
    username: str = Field(...)
    password: str = Field(...)
    role: int = Field(...)
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        """Config."""
        schema_extra = {
            "example": {
                "username": "example@gmail.com",
                "password": "abcd123456",
                "role": 0,
            }
        }
