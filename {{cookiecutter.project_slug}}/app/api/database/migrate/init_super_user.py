from fastapi.encoders import jsonable_encoder

from app.api.database.execute.user import user_execute as execute
from app.api.services import authentication_service
from app.core.constant import ADMIN_USER, SUPER_USERNAME, SUPER_PASSWORD


def init_super_user():
    if not execute.retrieve_data_by_role(ADMIN_USER):
        print("Create Super user...")
        user = {
            "username": str(SUPER_USERNAME),
            "password": str(SUPER_PASSWORD),
            "role": -1,
        }
        user = jsonable_encoder(user)
        user['password'] = authentication_service.get_password_hash(user['password'])
        execute.add_data(user)
