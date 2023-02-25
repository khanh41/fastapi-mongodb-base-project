"""Init superuser."""
from fastapi.encoders import jsonable_encoder

from app.api.database.execute.user import user_execute as execute
from app.api.services import authentication_service
from app.core.constant import ADMIN_USER, SUPER_PASSWORD, SUPER_USERNAME


def init_super_user():
    """Init superuser if not exist."""
    if not execute.retrieve_data_by_role(ADMIN_USER):
        print("Create Super user...")
        user = jsonable_encoder({
            "username": str(SUPER_USERNAME),
            "password": str(SUPER_PASSWORD),
            "role": -1,
        })
        user['password'] = authentication_service.get_password_hash(user['password'])
        execute.add_data(user)
