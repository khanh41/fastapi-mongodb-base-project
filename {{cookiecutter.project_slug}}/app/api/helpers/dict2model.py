"""Convert dictionary to model."""
from app.api.database.models.user import UserSchema


def convert_user_to_model(user_data: dict) -> UserSchema:
    """Convert user dictionary data to UserSchema."""
    user_data["userID"] = str(user_data.get("_id"))
    return UserSchema(**user_data)
