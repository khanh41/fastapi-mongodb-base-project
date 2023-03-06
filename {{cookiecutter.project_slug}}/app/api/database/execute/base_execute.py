"""Base Execute."""
from __future__ import annotations

import datetime

from bson.objectid import ObjectId


class BaseExecute:
    """Base Execute."""

    def __init__(self, data_collection, data_helper):
        self.data_collection = data_collection
        self.data_helper = data_helper

    def retrieve_datas(self):
        """Retrieve all data."""
        datas = []
        for data in self.data_collection.find():
            datas.append(self.data_helper(data))
        return datas

    def add_data(self, data: dict) -> dict:
        """Add a new data."""
        data['createAt'] = datetime.datetime.now()
        data['updateAt'] = datetime.datetime.now()
        data = self.data_collection.insert_one(data)
        new_data = self.data_collection.find_one({"_id": data.inserted_id})
        return self.data_helper(new_data)

    def retrieve_data(self, object_id: str) -> dict | None:
        """Retrieve a data with a matching ID."""
        data = self.data_collection.find_one({"_id": ObjectId(object_id)})
        if data:
            return self.data_helper(data)
        return None

    def update_data(self, object_id: str, data: dict) -> bool | None:
        """Update a data with a matching ID."""
        # Return false if an empty request body is sent.
        if len(data) < 1:
            return False

        data['updateAt'] = datetime.datetime.now()
        data = self.data_collection.find_one({"_id": ObjectId(object_id)})
        if data:
            updated_data = self.data_collection.update_one(
                {"_id": ObjectId(object_id)}, {"$set": data}
            )
            if updated_data:
                return True
            return False
        return None

    def delete_data(self, object_id: str) -> bool | None:
        """Delete a data."""
        data = self.data_collection.find_one({"_id": ObjectId(object_id)})
        if data:
            self.data_collection.delete_one({"_id": ObjectId(object_id)})
            return True
        return None
