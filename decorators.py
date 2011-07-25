def notify(f):
    def g(self, n):
        print n
        return f(self, n)
    return g

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @notify
    def scale(self, n):
        self.x = n * self.x
        self.y = n * self.y

p = Point(2.0, 3.0)
p.scale(2.5)
