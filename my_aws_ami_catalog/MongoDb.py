from pymongo import MongoClient
from my_aws_ami_catalog.MongodbConnectionString import MongodbConnectionString
import pymongo

class MongoDb:

    def save(self, dataList: list):
        mongodbConnectionString = MongodbConnectionString()
        
        CONNECTION_STRING = mongodbConnectionString.getString()
        client = MongoClient(CONNECTION_STRING)
        database = client["aws"]
        collection = database["amis"]
        collection.insert_many(dataList)

