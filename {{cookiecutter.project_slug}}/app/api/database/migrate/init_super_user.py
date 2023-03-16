"""Init superuser."""
from __future__ import annotations

import datetime
from typing import Any

from fastapi.encoders import jsonable_encoder

from app.api.database.execute.user import user_execute as execute
from app.api.helpers.dict2model import convert_user_to_model
from app.api.services import authentication_service
from app.core.constant import ADMIN_USER, SUPER_PASSWORD, SUPER_USERNAME


def init_super_user():
    """Init superuser if not exist."""
    if not execute.retrieve_data_by_role(ADMIN_USER):
        print("Create Super user...")
        user: dict[str, Any] = jsonable_encoder({
            "username": str(SUPER_USERNAME),
            "password": str(SUPER_PASSWORD),
            "role": -1,
        })
        user['password'] = authentication_service.get_password_hash(user['password'])
        user['createAt'] = datetime.datetime.now()
        user['updateAt'] = datetime.datetime.now()

        execute.add_data(convert_user_to_model(user))
