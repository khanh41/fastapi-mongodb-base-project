import ast
import os
import zipfile

import wget


def base_file_download(path_check, url_download):
    if not os.path.isfile(path_check):
        wget.download(url_download, path_check)


def base_zip_download(path_check, url_download):
    if not os.path.isdir(path_check):
        os.makedirs(path_check)
    if len(os.listdir(path_check)) <= 0:
        zip_path = wget.download(url_download, path_check + ".zip")
        with zipfile.ZipFile(zip_path, "r") as f:
            f.extractall(os.path.dirname(zip_path))


def base_zip_folder_download(path_check, url_download):
    if not os.path.isdir(path_check):
        zip_path = wget.download(url_download, path_check + ".zip")
        with zipfile.ZipFile(zip_path, "r") as f:
            f.extractall(os.path.dirname(zip_path))


def convert_string_to_list(coordinates_text: str):
    coordinates_text = coordinates_text.replace(" ", "")
    try:
        return ast.literal_eval(coordinates_text)
    except:
        raise ValueError("coordinates_text is string of list, example: \"[[1,2,3,4],[1,2,3,4]]\"")
