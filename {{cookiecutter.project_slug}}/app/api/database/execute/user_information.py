from app.api.database.connect import user_information_collection
from app.api.database.execute.base_execute import BaseExecute
from app.api.helpers.convert_model2dict import user_information_helper


class ExerciseTrainerExecute(BaseExecute):

    def __init__(self, data_collection, data_helper):
        super().__init__(data_collection, data_helper)


user_information_execute = ExerciseTrainerExecute(user_information_collection, user_information_helper)
