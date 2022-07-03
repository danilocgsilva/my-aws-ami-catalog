class DictParameterAssembly:

    def __init__(self):
        self.dictData = {}

    def get(self) -> dict:
        return self.dictData

    def addFilter(self, value: str, filter: str):
        filter_dict = {
            "Name": filter,
            "Values": [ value ]
        }

        if self.dictData == {}:
            self.dictData = self.dictData = {
                "Filters": [ filter_dict ]
            }
        else:
            self.dictData["Filters"].append(filter_dict)
