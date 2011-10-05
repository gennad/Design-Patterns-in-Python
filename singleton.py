# ---------- Singletone ----------


# Real Singleton instance
class Singleton(object):
    def __new__(type):
        if not '_the_instance' in type.__dict__:
            type._the_instance = object.__new__(type)
        return type._the_instance

a = Singleton()
a.toto = 12

b = Singleton()
print b.toto
print id(a), id(b)  # The same !!


# ---------- Borg's singletone ----------
class Borg:
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state

a = Borg()
a.toto = 12

b = Borg()
print b.toto
print id(a), id(b)  # different ! but states are sames

# ---------- Alex's Martelli examples ----------

class Singleton(object):
    def __new__(cls, *a, **k):
        if not hasattr(cls, '_inst'):
            cls._inst = super(Singleton, cls
).__new__(cls, *a, **k)
        return cls._inst

class Borg(object):
    """Subclassing is no problem."""
    _shared_state = {}
    def __new__(cls, *a, **k):
        obj = super(Borg, cls).__new__(cls, *a, **k)
        obj.__dict__ = cls._shared_state
        return obj
