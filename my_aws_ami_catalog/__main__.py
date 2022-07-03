from typing import Dict
from my_aws_ami_catalog.MAAC import MAAC
from my_aws_ami_catalog.DictParameterAssembly import DictParameterAssembly
import argparse
import json

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--filters-pairs",
        "-p"
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
    print(json.dumps(results, indent = 4))
