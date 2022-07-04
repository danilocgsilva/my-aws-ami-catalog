# My AWS AMI catalog

If you want to automates some of yours process regarding the virtual machine handling, choosing a *machine receipt* from the AWS may be troublesome.

You can use the aws cli or boto3, and may have some features that may help the task. But still you are very limited to the way to browse and fetch data if you relay only on the default filters provided by aws.

A better way is to fetches data from aws and stores in a local storage, with better options to data handling, as thos from a relational database or even non-relational.

## What this package provides?

Two stuffs:

* Command line installable utility: more easily fetches data from aws for listing amis from AWS.

You can install going to project folder and installing typing `pip install .`. This will install a command line that can be called just typing `maac`.

CAUTION! The default behaviour, and if when you provides any argument, will fetch all available AWS AMI data, what so much data. If parsed to json string, it takes at the time of this writing, more than 200 MB! And will take relativelly a long time, consume a huge amount of memory and processing to parse everything! But even in such situation, may be something that you eventually want!

What is expected is that you use this utility accompanied of parameter to provides some filter.

You can call this utility typing:
```
maac --filters-pairs architecture:arm64,description:*ubuntu*
```
This is an example of utility utilization, in which you add to filter the architecture beign the `arm64` and the ami description that is `*ubuntu*`

You have the option to add `--mongodb` as an option. This way, you may save the fetched data into a localhost mongo server.

* Utility to be used by other python utilities

We got two important objects: `MAAC` and `DictParameterAssembly`. The command line utlity uses both behind the scenes.

`MAAC` is the object that will fetches the data from AWS. It have the `fetch` method that fetches the aws data from AWS, BUT DOES NOT RETURNS ANYTHING. We also have the `getData` method, which will truly returns the data after `fetch` invocation.

`fetch` method may receive the raw dict that is used by AWS client to filter data. To generate this dict, we have the `DictParameterAssembly` that will assembly this dict. This class have the `addFilter` method, that receives the *filter value* as the first parameter, and the *filter name* as the second one. You can use this method several times to put any amount of filters in the same dict. Then, after you putted all the filters that you want, them just use the `get` method to get the dict that will be used in `MAAC` when fetching the data.
