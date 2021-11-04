import datetime

from bson.objectid import ObjectId


class BaseExecute(object):
    def __init__(self, data_collection, data_helper):
        self.data_collection = data_collection
        self.data_helper = data_helper

    # Retrieve all data
    def retrieve_datas(self):
        datas = []
        for data in self.data_collection.find():
            datas.append(self.data_helper(data))
        return datas

    # Add a new data
    def add_data(self, data: dict) -> dict:
        data['createAt'] = datetime.datetime.now()
        data['updateAt'] = datetime.datetime.now()
        data = self.data_collection.insert_one(data)
        new_data = self.data_collection.find_one({"_id": data.inserted_id})
        return self.data_helper(new_data)

    # Retrieve a data with a matching ID
    def retrieve_data(self, id: str) -> dict:
        data = self.data_collection.find_one({"_id": ObjectId(id)})
        if data:
            return self.data_helper(data)

    # Update a data with a matching ID
    def update_data(self, id: str, data: dict):
        # Return false if an empty request body is sent.
        if len(data) < 1:
            return False

        data['updateAt'] = datetime.datetime.now()
        data = self.data_collection.find_one({"_id": ObjectId(id)})
        if data:
            updated_data = self.data_collection.update_one(
                {"_id": ObjectId(id)}, {"$set": data}
            )
            if updated_data:
                return True
            return False

    # Delete a data
    def delete_data(self, id: str):
        data = self.data_collection.find_one({"_id": ObjectId(id)})
        if data:
            self.data_collection.delete_one({"_id": ObjectId(id)})
            return True
