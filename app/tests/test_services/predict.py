import joblib
import pandas as pd

from core.ml_configs import custom_column_constants
from core.ml_configs.config import AIKeibaConfigs

config = AIKeibaConfigs.get()


class Predict:
    @staticmethod
    def _predict(model, df):
        return model.predict(df.loc[:, ~df.columns.isin(["raceID"])])

    def predict(self, data: pd.DataFrame) -> pd.Series:
        # Load encoder
        encoder = joblib.load(config["base"]["encoder"])
        # Load model
        model = joblib.load(config["base"]["base_model"])
        # Load data
        # x_test = pd.read_csv(data)
        # Encoder
        data_trans = encoder.transform(data[custom_column_constants._CBE_COLUMNS])
        # Add raceID
        data_trans["raceID"] = data["raceID"]
        # Predict
        predictions = data_trans.groupby("raceID").apply(
            lambda x: self._predict(model, x)
        )

        return predictions, data_trans


"""    def predict_top6(self, predictions: pd.Series) -> pd.Series:
        pred_top6 = []
        for i in range(predictions.shape[0]):
            pred_top6_1_race = np.argsort(predictions.iloc[i])[:6]
            pred_top6.append(list(pred_top6_1_race))
        return pred_top6

def main():
    print('ok')"""


if __name__ == "__main__":
    main()
