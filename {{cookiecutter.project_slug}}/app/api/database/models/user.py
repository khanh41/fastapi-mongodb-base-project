from typing import Optional

from pydantic import BaseModel, Field


class UserSchema(BaseModel):
    username: str = Field(...)
    password: str = Field(...)
    role: int = Field(...)
    createAt: Optional[str] = None
    updateAt: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "username": "example@gmail.com",
                "password": "abcd123456",
                "role": 0,
            }
        }
