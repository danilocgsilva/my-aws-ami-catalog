import boto3
import argparse

class MAAC:

    def __init__(self):
        self.dataFetched = None
        self.profile = None
    
    def fetch(self, params = {}):

        if self.profile:
            boto3.setup_default_session(profile_name=self.profile)
        
        ec2Client = boto3.client("ec2")
        self.dataFetched = ec2Client.describe_images(**params)["Images"]

    def getData(self) -> dict:
        return self.dataFetched

    def setProfile(self, profile: str):
        self.profile = profile
        return self
