from typing import Optional

from pydantic import BaseModel
from pydantic import Field


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


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class UserInDB(UserSchema):
    hashed_password: str
