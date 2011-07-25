# Toy-example facade
class LifoStack:
    def __init__(self):
        self._stack = []

    def push(self, datum):
        self._stack.append(datum)

    def pop(self):
        return self._stack.pop()
