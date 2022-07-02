from my_aws_ami_catalog.MAAC import MAAC

def main():
    maac = MAAC()
    results = maac.fetch()
    print(results)

