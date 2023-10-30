"""User Execute Define."""
from __future__ import annotations

from app.api.database.connect import user_collection
from app.api.database.execute.base_execute import BaseExecute
from app.api.database.models.user import UserSchema
from app.api.helpers.dict2model import convert_user_to_model


class UserExecute(BaseExecute):
    """User Execute."""

    def retrieve_data_by_username(self, username: str) -> UserSchema | None:
        """Get user information by a username."""
        if data := self.data_collection.find_one({"username": username}):
            return self.convert_helper(data)
        return None

    def retrieve_data_by_role(self, role: int) -> UserSchema | None:
        """Get user information by a role."""
        if data := self.data_collection.find_one({"role": role}):
            return self.convert_helper(data)
        return None


user_execute = UserExecute(user_collection, convert_user_to_model)
