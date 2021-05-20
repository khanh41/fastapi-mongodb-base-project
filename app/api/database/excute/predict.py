from bson.objectid import ObjectId

from app.api.database.connect import predict_collection
from app.api.helpers.convert_model2dict import predict_helper


# Retrieve all predicts present in the database
def retrieve_predicts():
    predicts = []
    for predict in predict_collection.find():
        predicts.append(predict_helper(predict))
    return predicts


# Add a new predict into to the database
def add_predict(predict_data: dict) -> dict:
    predict = predict_collection.insert_one(predict_data)
    new_predict = predict_collection.find_one({"_id": predict.inserted_id})
    return predict_helper(new_predict)


# Retrieve a predict with a matching ID
def retrieve_predict(id: str) -> dict:
    predict = predict_collection.find_one({"_id": ObjectId(id)})
    if predict:
        return predict_helper(predict)


# Retrieve a predict with a matching ID
def retrieves_predict_by_race_id(id: str) -> dict:
    predicts = []
    for predict in predict_collection.find({"raceID": id}):
        predicts.append(predict_helper(predict))
    return predicts


# Update a predict with a matching ID
def update_predict(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    predict = predict_collection.find_one({"_id": ObjectId(id)})
    if predict:
        updated_predict = predict_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_predict:
            return True
        return False


# Delete a predict from the database
def delete_predict(id: str):
    predict = predict_collection.find_one({"_id": ObjectId(id)})
    if predict:
        predict_collection.delete_one({"_id": ObjectId(id)})
        return True
