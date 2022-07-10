from typing import Dict
from my_aws_ami_catalog.MAAC import MAAC
from my_aws_ami_catalog.DictParameterAssembly import DictParameterAssembly
from my_aws_ami_catalog.MongoDb import MongoDb
import argparse
import json
from getpass import getpass

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--filters-pairs",
        "-p"
    )
    parser.add_argument(
        "--mongodb",
        "-m",
        required=False,
        action="store_true"
    )
    parser.add_argument(
        "--mongodb-credentials",
        "-c",
        required=False,
        action="store_true"
    )

    args = parser.parse_args()
    
    if args.filters_pairs:
        filters_pairs_cutted = args.filters_pairs.split(",")

        dictParameterAssembly = DictParameterAssembly()

        for filter_pair in filters_pairs_cutted:
            members = filter_pair.split(":")
            dictParameterAssembly.addFilter(members[1], members[0])
        filters_for_maac = dictParameterAssembly.get()
    else:
        filters_for_maac = {}

    maac = MAAC()
    maac.fetch(filters_for_maac)
    results = maac.getData()

    if not args.mongodb:
        print(json.dumps(results, indent = 4))
        print("---")
    else:
        mongodb = MongoDb()

        if args.mongodb_credentials:
            set_credentials(mongodb)

        mongodb.save(results)

    print("We got " + str(len(results)) + " instances ami.")

def set_credentials(mongodb):
    mongodb.setUser(input("Please, set the user name: "))
    mongodb.setPassword(getpass("Please, set the user password: "))
