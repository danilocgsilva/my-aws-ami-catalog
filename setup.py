from setuptools import setup

VERSION = "0.0.1"

def readme():
    with open("README.md") as f:
        return f.read()

setup(
    name="my_aws_ami_catalog",
    version=VERSION,
    description="Facilitates fetches and storage aws ami data from AWS",
    long_description_content_type="text/markdown",
    long_description=readme(),
    keywords="AWS AMI storage",
    url="https://github.com/danilocgsilva/my-aws-ami-catalog",
    author="Danilo Silva",
    author_email="contact@danilocgsilva.me",
    packages=["my_aws_ami_catalog"],
    entry_points={"console_scripts": ["maac=my_aws_ami_catalog.__main__:main"],},
    include_package_data=True
)

