import unittest
from my_aws_ami_catalog.DictParameterAssembly import DictParameterAssembly

class testDictParameterAssemblyTest(unittest.TestCase):

    def setUp(self):
        self.dictParameterAssembly = DictParameterAssembly()

    def testBasicParameter(self):
        expected_result = {}
        object_result = self.dictParameterAssembly.get()
        self.assertEqual(expected_result, object_result)

    def testWantArm(self):

        self.dictParameterAssembly.addFilter("arm64", "architecture")

        expected_result = {
            "Filters": [
                {
                    "Name": "architecture",
                    "Values": [
                        "arm64"
                    ]
                }
            ]
        }

        object_result = self.dictParameterAssembly.get()
        self.assertEqual(expected_result, object_result)

    def testWantx86(self):
        self.dictParameterAssembly.addFilter("x86", "architecture")

        expected_result = {
            "Filters": [
                {
                    "Name": "architecture",
                    "Values": [
                        "x86"
                    ]
                }
            ]
        }

        object_result = self.dictParameterAssembly.get()
        self.assertEqual(expected_result, object_result)

    def testAddDescription2204(self):
        self.dictParameterAssembly.addFilter("*22.04*", "description")

        expected_result = {
            "Filters": [
                {
                    "Name": "description",
                    "Values": [
                        "*22.04*"
                    ]
                }
            ]
        }

        object_result = self.dictParameterAssembly.get()
        self.assertEqual(expected_result, object_result)

    def testAddDescriptionAndArchiteture(self):
        self.dictParameterAssembly.addFilter("*ubuntu*", "description")
        self.dictParameterAssembly.addFilter("x86_64", "architecture")
    
        expected_result = {
            "Filters": [
                {
                    "Name": "description",
                    "Values": [
                        "*ubuntu*"
                    ]
                },
                {
                    "Name": "architecture",
                    "Values": [
                        "x86_64"
                    ]
                }
            ]
        }

        object_result = self.dictParameterAssembly.get()

        self.assertEqual(object_result, expected_result)

if __name__ == '__main__':
    unittest.main()
