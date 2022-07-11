from pymongo import MongoClient
from my_aws_ami_catalog.MongodbConnectionString import MongodbConnectionString
import pymongo

class MongoDb:

    def __init__(self):
        self.mongodb_user = None
        self.mongodb_password = None
        self.port = None

    def setUser(self, user: str):
        self.mongodb_user = user
        return self

    def setPassword(self, password: str):
        self.mongodb_password = password
        return self

    def setPort(self, port: int):
        self.port = port
        return self

    def save(self, dataList: list):
        mongodbConnectionString = MongodbConnectionString()

        if self.mongodb_user:
            mongodbConnectionString.setUser(self.mongodb_user)

        if self.mongodb_password:
            mongodbConnectionString.setPassword(self.mongodb_password)

        if self.port:
            mongodbConnectionString.setPort(self.port)

        CONNECTION_STRING = mongodbConnectionString.getString()
        client = MongoClient(CONNECTION_STRING)
        database = client["aws"]
        collection = database["amis"]
        collection.insert_many(dataList)

