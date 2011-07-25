class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def scale(self, n):
        self.x = n * self.x
        self.y = n * self.y

def notify(f):
    def g(self, n):
        print n
        return f(self, n)
    return g

Point.scale = notify(Point.scale)
p = Point(2.0, 3.0)
p.scale(2.5)
