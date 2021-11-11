from typing import Optional

from pydantic import BaseModel, Field


class UserInformationSchema(BaseModel):
    userId: str = Field(...)
    name: str = Field(...)
    email: str = Field(...)
    phoneNumber: str = Field(...)
    age: int = Field(...)
    createAt: Optional[str] = None
    updateAt: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "userId": "1233",
                "name": "example",
                "email": "example@gmail.com",
                "phoneNumber": "0123456789",
                "age": 22,
            }
        }
