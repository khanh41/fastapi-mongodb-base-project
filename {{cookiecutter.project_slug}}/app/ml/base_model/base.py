import abc


class BaseModel(abc.ABC):
    model = None

    @abc.abstractmethod
    def create_model(self):
        pass

    @abc.abstractmethod
    def compile(self):
        pass

    @abc.abstractmethod
    def preprocess_input(self):
        pass

    @abc.abstractmethod
    def fit(self, train_dataset, epochs, val_dataset):
        pass

    @abc.abstractmethod
    def predict(self, images):
        pass

    @abc.abstractmethod
    def evaluate(self, test_dataset):
        pass

    def save_model(self, save_path):
        self.model.save_weights(save_path)
