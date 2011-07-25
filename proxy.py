class JustInTimeCreator:
    def __init__(self, cls, *a, **k):
        self._m = cls, a, k

    def __getattr__(self, name):
        if not hasattr(self, '_x'):
            cls, a, k = self._m
            self._x = cls(*a, **k)
        return getattr(self._x, name)
