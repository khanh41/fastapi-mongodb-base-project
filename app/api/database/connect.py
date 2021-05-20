import os

import pymongo

# Connect mysql to read db from server - tracking

# Connect mongodb - save data tracking and predict
client = pymongo.MongoClient(os.getenv("MONGO_DETAILS"))
database = client.keiba_db
race_collection = database.get_collection("race")
horse_collection = database.get_collection("horses")
predict_collection = database.get_collection("predict")
