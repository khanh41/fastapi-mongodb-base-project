# skip-file
"""Token Models."""
from typing import Optional as Op

from app.api.database.models.base import CustomBaseModel


class Token(CustomBaseModel):
    """Token Model."""
    access_token: str
    token_type: str


class TokenData(CustomBaseModel):
    """Token Data."""
    username: Op[str] = None
