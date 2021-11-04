from app.api.database.connect import user_exercise_collection
from app.api.database.execute.base_execute import BaseExecute
from app.api.helpers.convert_model2dict import user_exercise_helper


class UserExerciseExecute(BaseExecute):

    def __init__(self, data_collection, data_helper):
        super().__init__(data_collection, data_helper)


user_exercise_execute = UserExerciseExecute(user_exercise_collection, user_exercise_helper)
