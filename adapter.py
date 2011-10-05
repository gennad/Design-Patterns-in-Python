class Adaptee:
    def specific_request(self):
        return 'Adaptee'

class Adapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        return self.adaptee.specific_request()

client = Adapter(Adaptee())
print client.request()

# --------- Second example (by Alex Martelli)------------

class UppercasingFile:
    def __init__(self, *a, **k):
        self.f = file(*a, **k)

    def write(self, data):
        self.f.write(data.upper())

    def __getattr__(self, name):
        return getattr(self.f, name)
