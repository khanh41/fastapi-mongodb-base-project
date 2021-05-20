def predict_helper(data) -> dict:
    return {
        "id": str(data["_id"]),
        "raceID": data["raceID"],
        "timePredict": data["timePredict"],
        "typePredict": data["typePredict"],
        "status": data["status"],
        "horseRank": data["horseRank"],
        "lastFinalRank": data["lastFinalRank"],
    }
