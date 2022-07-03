from my_aws_ami_catalog.MAAC import MAAC

class MongoDb:

    def setMAAC(self, maac: MAAC):
        self.maac = maac
        return self
