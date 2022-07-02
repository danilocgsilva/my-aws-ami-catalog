import boto3
import argparse

class MAAC:

    def __init__(self):
        self.dataFetched = None
    
    def fetch(self, params = {}):
        ec2Client = boto3.client("ec2")
        self.dataFetched = ec2Client.describe_images(**params)["Imagess"]

    def getData(self) -> dict:
        return self.dataFetched
