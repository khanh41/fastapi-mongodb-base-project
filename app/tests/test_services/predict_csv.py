import numpy as np
import pandas as pd
from predict import Predict

from core.ml_configs.config import AIKeibaConfigs

config = AIKeibaConfigs.get()


def predict_csv():
    # Load data
    path = config["dataset"]["data_predict"]
    data = pd.read_csv(path)
    print(f"Shape data: {data.shape}")
    print(data.dtypes)

    predictions, data = Predict().predict(data)
    ai_predict_df = pd.DataFrame()
    X_test_groupby = data.groupby("raceID")
    for key, item in X_test_groupby:
        test_group = X_test_groupby.get_group(key)
        pred_top6 = np.argsort(predictions[key])[:6]
        ai_predict = test_group.iloc[pred_top6][["raceID", "horseNo"]]
        ai_predict_df = ai_predict_df.append(ai_predict)
    print(type(ai_predict))
    print(ai_predict_df)
    ai_predict_df.to_excel("result.xlsx", index=False)
    print("OK")


if __name__ == "__main__":
    predict_csv()
