class MongodbConnectionString:

    def __init__(self):
        self.address = None
        self.srv = False

    def setAddress(self, address: str):
        self.address = address

    def setSrv(self):
        self.srv = True

    def getString(self) -> str:
        base_string = "mongodb{}://{}:27017/"

        srv_replacement = "+srv" if self.srv else ""
        address_replacement = self.address if self.address else "127.0.0.1"

        return base_string.format(srv_replacement, address_replacement)
