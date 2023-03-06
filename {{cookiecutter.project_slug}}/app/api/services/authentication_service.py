"""Authentication service."""
from __future__ import annotations

from datetime import datetime, timedelta
from typing import Optional as Op

from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt

from app.api.database.execute.user import user_execute as execute
from app.api.database.models.user import (
    TokenData,
    UserInDB,
    UserSchema,
    oauth2_scheme,
    pwd_context,
)
from app.core.constant import ALGORITHM, SECRET_KEY


async def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    """Check login token of current user."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError as exc:
        raise credentials_exception from exc

    user = execute.retrieve_data_by_username(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify password."""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """Password to hash password"""
    return pwd_context.hash(password)


def authenticate_user(username: str, password: str) -> bool | UserInDB:
    """Authenticate user."""
    user = execute.retrieve_data_by_username(username)
    user = UserInDB(**user)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Op[timedelta] = None) -> str:
    """Create access token."""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_active_user(current_user: UserSchema = Depends(get_current_user)) -> UserSchema:
    """Get current active user."""
    return current_user
