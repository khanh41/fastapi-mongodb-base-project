import os

import pymongo

client = pymongo.MongoClient(os.getenv("MONGO_DETAILS"), serverSelectionTimeoutMS=5000)

database = client.test
# database = client.{{ cookiecutter.project_slug}}

user_collection = database.get_collection("user")
