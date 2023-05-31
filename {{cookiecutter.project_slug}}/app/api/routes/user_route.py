"""User route."""
from fastapi import APIRouter, Body

from app.api.database.execute.user import user_execute as execute
from app.api.database.models.user import UserSchema
from app.api.responses.base import BaseResponse
from app.api.responses.model2reponse import convert_user_model_to_response
from app.api.services import user_service

router = APIRouter()


@router.post("", response_description="user data added into the database")
async def add_user_data(user: UserSchema = Body(...)):
    """Add user data to database."""
    return BaseResponse.success_response(data=user_service.add_user(user))


@router.get("", response_description="users retrieved")
async def get_users():
    """Get all user's information."""
    users = execute.retrieve_datas()
    return BaseResponse.success_response(data=[convert_user_model_to_response(user) for user in users])


@router.get("/{user_id}", response_description="user data retrieved")
async def get_user_data(user_id: str):
    """Get user information by id."""
    if user := execute.retrieve_data(user_id):
        return BaseResponse.success_response(data=convert_user_model_to_response(user))
    return BaseResponse.error_response(f"user {user_id} doesn't exist.", 404)


@router.put("/{user_id}")
async def update_user_data(user_id: str, req: UserSchema = Body(...)):
    """Update user data."""
    req = {k: v for k, v in req.dict().items() if v is not None}
    if updated_user := execute.update_data(user_id, req):
        return BaseResponse.success_response(message=f"successful user update with ID {user_id}")
    return BaseResponse.error_response("There was an error updating the user data.", 404)


@router.delete("/{user_id}", response_description="user data deleted from the database")
async def delete_user_data(user_id: str):
    """Delete user data by user id."""
    if deleted_user := execute.delete_data(user_id):
        return BaseResponse.success_response(message=f"user with ID: {user_id} removed")
    return BaseResponse.error_response(f"user with id {user_id} doesn't exist", 404)
