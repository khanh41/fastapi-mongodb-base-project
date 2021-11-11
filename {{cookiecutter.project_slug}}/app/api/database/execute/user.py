from app.api.database.connect import user_collection
from app.api.database.execute.base_execute import BaseExecute
from app.api.helpers.convert_model2dict import user_helper


class UserExecute(BaseExecute):

    def __init__(self, data_collection, data_helper):
        super().__init__(data_collection, data_helper)

    # Retrieve a data with a matching email
    def retrieve_data_by_username(self, username: str) -> dict:
        data = self.data_collection.find_one({"username": username})
        if data:
            return self.data_helper(data)

    def retrieve_data_by_role(self, role: int) -> dict:
        data = self.data_collection.find_one({"role": role})
        if data:
            return self.data_helper(data)


user_execute = UserExecute(user_collection, user_helper)
