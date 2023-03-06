"""User Execute Define."""
from __future__ import annotations

from app.api.database.connect import user_collection
from app.api.database.execute.base_execute import BaseExecute
from app.api.helpers.convert_model2dict import user_helper


class UserExecute(BaseExecute):
    """User Execute."""

    # Retrieve a data with a matching email
    def retrieve_data_by_username(self, username: str) -> dict | None:
        """Get user information by username."""
        data = self.data_collection.find_one({"username": username})
        if data:
            return self.data_helper(data)
        return None

    def retrieve_data_by_role(self, role: int) -> dict | None:
        """Get user information by role."""
        data = self.data_collection.find_one({"role": role})
        if data:
            return self.data_helper(data)
        return None


user_execute = UserExecute(user_collection, user_helper)
