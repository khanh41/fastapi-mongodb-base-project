from app.api.database.connect import exercise_collection
from app.api.database.execute.base_execute import BaseExecute
from app.api.helpers.convert_model2dict import exercise_helper


class ExerciseExecute(BaseExecute):

    def __init__(self, data_collection, data_helper):
        super().__init__(data_collection, data_helper)


exercise_execute = ExerciseExecute(exercise_collection, exercise_helper)
