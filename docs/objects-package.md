# Object packages

With this utility you can also have a package to be used by other python utilities.

We got two important objects: `MAAC` and `DictParameterAssembly`. The command line utlity uses both behind the scenes.

`MAAC` is the object that will fetches the data from AWS. It have the `fetch` method that fetches the aws data from AWS, BUT DOES NOT RETURNS ANYTHING. We also have the `getData` method, which will truly returns the data after `fetch` invocation.

`fetch` method may receive the raw dict that is used by AWS client to filter data. To generate this dict, we have the `DictParameterAssembly` that will assembly this dict. This class have the `addFilter` method, that receives the *filter value* as the first parameter, and the *filter name* as the second one. You can use this method several times to put any amount of filters in the same dict. Then, after you putted all the filters that you want, them just use the `get` method to get the dict that will be used in `MAAC` when fetching the data.

