"""Base Execute."""
from __future__ import annotations

from bson.objectid import ObjectId

from app.api.database.models.base import CustomBaseModel


class BaseExecute:
    """Base Execute."""

    def __init__(self, data_collection, convert_helper):
        self.data_collection = data_collection
        self.convert_helper = convert_helper

    def retrieve_datas(self) -> list[CustomBaseModel]:
        """Retrieve all data."""
        return [self.convert_helper(data) for data in self.data_collection.find()]

    def add_data(self, data: CustomBaseModel) -> CustomBaseModel:
        """Add a new data."""
        data = self.data_collection.insert_one(data.model_dump())
        new_data = self.data_collection.find_one({"_id": data.inserted_id})
        return self.convert_helper(new_data)

    def retrieve_data(self, object_id: str) -> CustomBaseModel | None:
        """Retrieve data with a matching ID."""
        if data := self.data_collection.find_one({"_id": ObjectId(object_id)}):
            return self.convert_helper(data)
        return None

    def update_data(self, object_id: str, update_data: dict) -> bool:
        """Update a data with a matching ID."""
        if self.data_collection.find_one({"_id": ObjectId(object_id)}):
            updated_data = self.data_collection.update_one({"_id": ObjectId(object_id)}, {"$set": update_data})
            return bool(updated_data)
        return False

    def delete_data(self, object_id: str) -> bool:
        """Delete a data."""
        if self.data_collection.find_one({"_id": ObjectId(object_id)}):
            self.data_collection.delete_one({"_id": ObjectId(object_id)})
            return True
        return False
