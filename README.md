# My AWS AMI catalog

If you want to automates some of yours process regarding the virtual machine handling, choosing a *machine receipt* from the AWS may be troublesome.

You can use the aws cli or boto3, and may have some features that may help the task. But still you are very limited to the way to browse and fetch data if you relay only on the default filters provided by aws scripts.

A better way is to fetches data from aws and stores in a local storage, with better options to data handling, as those from a relational database or even non-relational.

## What this package provides?

* [A command line utlity to do the tasks](docs/command-line.md)
* [A package to be used by other scripts](docs/objects-package.md)
