def user_information_helper(data) -> dict:
    return {
        "id": str(data["_id"]),
        "name": data["timePredict"],
        "email": data["email"],
        "phoneNumber": data["phoneNumber"],
        "weight": data["weight"],
        "createAt": str(data["createAt"]),
        "updateAt": str(data["updateAt"]),
    }


def user_helper(data) -> dict:
    return {
        "id": str(data["_id"]),
        "username": data["username"],
        "password": data["password"],
        "hashed_password": data["password"],
        "role": data["role"],
        "createAt": str(data["createAt"]),
        "updateAt": str(data["updateAt"]),
    }
