from app.api.database.connect import exercise_trainer_collection
from app.api.database.execute.base_execute import BaseExecute
from app.api.helpers.convert_model2dict import exercise_trainer_helper


class ExerciseTrainerExecute(BaseExecute):

    def __init__(self, data_collection, data_helper):
        super().__init__(data_collection, data_helper)


exercise_trainer_execute = ExerciseTrainerExecute(exercise_trainer_collection, exercise_trainer_helper)
