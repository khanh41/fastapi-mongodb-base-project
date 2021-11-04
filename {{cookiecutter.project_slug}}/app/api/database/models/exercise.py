from typing import Optional

from pydantic import BaseModel, Field


class ExerciseSchema(BaseModel):
    name: str = Field(...)
    level: int = Field(...)
    rating: int = Field(...)
    createAt: Optional[str] = None
    updateAt: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "name": "Push",
                "level": 1,
                "rating": 5,
            }
        }
