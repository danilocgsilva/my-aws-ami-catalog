class MongodbConnectionString:

    def __init__(self):
        self.address = None
        self.srv = False
        self.user = None
        self.password = None
        self.port = None

    def setAddress(self, address: str):
        self.address = address

    def setSrv(self):
        self.srv = True
        return self

    def setUser(self, user: str):
        self.user = user
        return self

    def setPassword(self, password: str):
        self.password = password
        return self

    def setPort(self, port: str):
        self.port = port
        return self

    def getString(self) -> str:
        base_string = "mongodb{}://{}{}:{}/"

        srv_replacement = "+srv" if self.srv else ""

        if self.user and self.password:
            user_password_replacement = self.user + ":" + self.password + "@"
        else:
            user_password_replacement = ""

        address_replacement = self.address if self.address else "127.0.0.1"

        port_replacement = self.port if self.port else "27017"

        return base_string.format(
            srv_replacement, 
            user_password_replacement, 
            address_replacement,
            port_replacement
        )
