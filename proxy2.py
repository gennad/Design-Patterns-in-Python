# -*- coding: utf-8 -*-

class IMath:
    """Интерфейс для прокси и реального субъекта"""
    def add(self, x, y):
        raise NotImplementedError()

    def sub(self, x, y):
        raise NotImplementedError()

    def mul(self, x, y):
        raise NotImplementedError()

    def div(self, x, y):
        raise NotImplementedError()

class Math(IMath):
    """Реальный субъект"""
    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def mul(self, x, y):
        return x * y

    def div(self, x, y):
        return x / y

class Proxy(IMath):
    """Прокси"""
    def __init__(self):
        self.math = Math()

    def add(self, x, y):
        return self.math.add(x, y)

    def sub(self, x, y):
        return self.math.sub(x, y)

    def mul(self, x, y):
        return self.math.mul(x, y)

    def div(self, x, y):
        if y == 0:
            return float('inf') # Вернуть positive infinity
        return self.math.div(x, y)

p = Proxy()
x, y = 4, 2
print '4 + 2 = ' + str(p.add(x, y))
print '4 - 2 = ' + str(p.sub(x, y))
print '4 * 2 = ' + str(p.mul(x, y))
print '4 / 2 = ' + str(p.div(x, y))
