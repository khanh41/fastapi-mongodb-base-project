def exercise_helper(data) -> dict:
    return {
        "id": str(data["_id"]),
        "name": data["name"],
        "level": data["level"],
        "rating": data["rating"],
        "createAt": str(data["createAt"]),
        "updateAt": str(data["updateAt"]),
    }


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


def user_exercise_helper(data) -> dict:
    return {
        "id": str(data["_id"]),
        "exerciseId": data["exerciseId"],
        "process": data["process"],
        "numStreak": data["numStreak"],
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


def exercise_trainer_helper(data) -> dict:
    return {
        "id": str(data["_id"]),
        "modelUrl": data["modelUrl"],
        "angleConfig": data["angleConfig"],
        "createAt": str(data["createAt"]),
        "updateAt": str(data["updateAt"]),
    }
