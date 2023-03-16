"""Convert model to response."""
from app.api.database.models.user import UserSchema


def convert_user_model_to_response(user: UserSchema):
    """Convert user model for response."""
    return {
        "userID": user.userID,
        "userName": user.username,
        "role": user.role,
        "createAt": user.createAt,
        "updateAt": user.updateAt,
    }
