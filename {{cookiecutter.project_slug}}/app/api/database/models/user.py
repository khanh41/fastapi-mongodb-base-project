# pylint: skip-file
"""User Model."""
from datetime import datetime
from typing import Optional

from pydantic import Field

from app.api.database.models.base import CustomBaseModel


class UserSchema(CustomBaseModel):
    """User Schema."""
    userID: Optional[str] = None
    username: str = Field(...)
    password: str = Field(...)
    role: int = Field(...)
    createAt: Optional[datetime] = None
    updateAt: Optional[datetime] = None

    class Config:
        """Config."""
        schema_extra = {
            "example": {
                "username": "example@gmail.com",
                "password": "abcd123456",
                "role": 0,
            }
        }
