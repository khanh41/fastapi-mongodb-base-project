from datetime import timedelta

from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.api.database.models.token import Token
from app.api.database.models.user import UserSchema
from app.api.services.authentication_service import authentication_service
from app.logger.logger import configure_logging

# to get a string like this run:
# openssl rand -hex 32

logger = configure_logging(__name__)
router = APIRouter()


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authentication_service.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=authentication_service.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = authentication_service.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/users/me/", response_model=UserSchema)
async def read_users_me(current_user: UserSchema):
    return current_user


@router.get("/users/me/items/")
async def read_own_items(current_user: UserSchema):
    return [{"item_id": "Foo", "owner": current_user.username}]
