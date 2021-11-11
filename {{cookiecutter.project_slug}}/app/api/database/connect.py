import pymongo

from app.core.constant import MONGO_DETAILS

client = pymongo.MongoClient(MONGO_DETAILS, serverSelectionTimeoutMS=5000)

database = client.test
# database = client.{{ cookiecutter.project_slug}}

user_collection = database.get_collection("user")
user_information_collection = database.get_collection("user_information")
