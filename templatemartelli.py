class AbstractBase(object):
    def orgMethod(self):
        self.doThis()
        self.doThat()

class Concrete(AbstractBase):
    def doThis(self):
        pass
    def doThat(self):
        pass

