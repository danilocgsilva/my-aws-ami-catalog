from pymongo import MongoClient
import pymongo

class MongoDb:

    def save(self, dataList: list):
        CONNECTION_STRING = "mongodb://127.0.0.1:27017/"
        client = MongoClient(CONNECTION_STRING)
        database = client["aws"]
        collection = database["amis"]
        collection.insert_many(dataList)

