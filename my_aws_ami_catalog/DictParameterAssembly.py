class DictParameterAssembly:

    def __init__(self):
        self.dictData = {}

    def get(self) -> dict:
        return self.dictData

    def addArchitecture(self, architecture: str):

        filter_dict = {
            "Name": "architecture",
            "Values": [ architecture ]
        }

        if self.dictData == {}:
            self.dictData = {
                "Filters": [
                    filter_dict
                ]
            }
        else:
            self.dictData["Filters"].append(filter_dict)

    def addDescription(self, description: str):

        filter_dict = {
            "Name": "description",
            "Values": [ description ]
        }

        if self.dictData == {}:
            self.dictData = self.dictData = {
                "Filters": [ filter_dict ]
            }
        else:
            self.dictData["Filters"].append(filter_dict)
