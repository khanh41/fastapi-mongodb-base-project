"""User Service."""
from datetime import datetime

from app.api.database.execute.user import user_execute
from app.api.database.models.user import UserSchema
from app.api.services import authentication_service


class UserService:
    """User Service."""

    @staticmethod
    def add_user(user: UserSchema):
        """Add user to database."""
        user_password = user.password
        user.password = authentication_service.get_password_hash(user_password)
        user.created_at = datetime.now()
        user.updated_at = datetime.now()

        new_user = user_execute.add_data(user)
        new_user.password = user_password
        return new_user
