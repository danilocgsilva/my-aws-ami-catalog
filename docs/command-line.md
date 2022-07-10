# Command line utility

More easily fetches data from aws for listing amis from AWS.

You can install going to project folder and installing typing `pip install .`. This will install a command line that can be called just typing `maac`.

CAUTION! The default behaviour, and if when you provides any argument, will fetch all available AWS AMI data, what so much data. If parsed to json string, it takes at the time of this writing, more than 200 MB! And will take relativelly a long time, consume a huge amount of memory and processing to parse everything! But even in such situation, may be something that you eventually want!

What is expected is that you use this utility accompanied of parameter to provides some filter.

You can call this utility typing:
```
maac --filters-pairs architecture:arm64,description:*ubuntu*
```
This is an example of utility utilization, in which you add to filter the architecture beign the `arm64` and the ami description that is `*ubuntu*`

## Saving data fetched directly to mongodb

You have the option to add `--mongodb` as an option. This way, you may save the fetched data into a localhost mongo server.