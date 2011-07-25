class UppercasingFile:
    def __init__(self, *a, **k):
        self.f = file(*a, **k)

    def write(self, data):
        self.f.write(data.upper())

    def __getattr__(self, name):
        return getattr(self.f, name)
