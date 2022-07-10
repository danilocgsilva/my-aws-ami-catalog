import unittest
from my_aws_ami_catalog.MongodbConnectionString import MongodbConnectionString

class testMongodbConnectionString(unittest.TestCase):

    def setUp(self):
        self.mongoConnectionString = MongodbConnectionString()

    def testDefaults(self):
        expected_string = "mongodb://127.0.0.1:27017/"
        self.assertEqual(expected_string, self.mongoConnectionString.getString())

    def testSetAdrress(self):
        self.mongoConnectionString.setAddress("171.252.77.24")        
        expected_string = "mongodb://171.252.77.24:27017/"
        self.assertEqual(expected_string, self.mongoConnectionString.getString())

    def testSetSrv(self):
        self.mongoConnectionString.setSrv()
        expected_string = "mongodb+srv://127.0.0.1:27017/"
        self.assertEqual(expected_string, self.mongoConnectionString.getString())

    def testAddUserAndPasswordAuthentication(self):
        self.mongoConnectionString.setUser("root")
        self.mongoConnectionString.setPassword("example")
        expected_string = "mongodb://root:example@127.0.0.1:27017/"
        self.assertEqual(expected_string, self.mongoConnectionString.getString())

