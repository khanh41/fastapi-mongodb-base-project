"""Convert model to response."""
from app.api.database.models.user import UserSchema


def convert_user_model_to_response(user: UserSchema):
    """Convert user model for response."""
    return {
        "user_id": user.user_id,
        "username": user.username,
        "role": user.role,
        "createAt": user.created_at,
        "updateAt": user.updated_at,
    }
