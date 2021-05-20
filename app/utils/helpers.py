import json

import numpy as np
import pandas as pd


def load_csv(csv_path: str) -> pd.DataFrame:
    """
    @param csv_path:
    @return:
    """
    data = pd.read_csv(
        filepath_or_buffer=csv_path, index_col=0, sep=";", low_memory=False
    )
    return data


def write_csv(csv_path: str, data: pd.DataFrame):
    """
    @param csv_path:
    @param data:
    @return:
    """
    data.to_csv(path_or_buf=csv_path, index=False, header=True)


def load_json(json_path: str) -> dict:
    """
    @param json_path:
    @return:
    """
    with open(json_path, "r") as file:
        return json.loads(file.read())


def write_json(json_file: str, data: dict):
    """
    @param json_file:
    @param data:
    @return:
    """
    with open(json_file, "w") as file:
        json.dump(data, file, indent=4)


def merge_data(
    data: pd.DataFrame, other_data: pd.DataFrame, left_on: str, right_on: str
) -> pd.DataFrame:
    """
    Merge data from two tables
    @param data: first table
    @param other_data: second table
    @param left_on: data key
    @param right_on: other data key
    @return: Data are merged from two tables
    """
    return pd.merge(left=data, right=other_data, left_on=left_on, right_on=right_on)


def create_group(data: pd.DataFrame) -> list:
    """

    @param data: Data
    @return: list group data for train XGBoostRanker
    """
    group = data.groupby("raceID").size().to_frame("size")["size"].to_numpy()

    return group


def save_numpy(numpy_name_file: str, data):
    """
    :param numpy_name_file:
    :param data:
    :return:
    """
    np.save(numpy_name_file, data)


def load_numpy(numpy_path: str):
    """
    @param numpy_path:
    @return:
    """
    data = np.load(numpy_path, allow_pickle=True)
    return data
