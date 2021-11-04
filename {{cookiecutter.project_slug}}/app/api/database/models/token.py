from typing import Optional

from pydantic import BaseModel

from app.api.database.models.user import UserSchema


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class UserInDB(UserSchema):
    hashed_password: str
