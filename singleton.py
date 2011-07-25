# http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/66531
class Borg:
    __shared_state = {}
    def __init__(self):
        self.__dict__ = self.__shared_state

a=Borg()
a.toto = 12

b=Borg()
print b.toto
print id(a),id(b) # different ! but states are sames



real Singleton instance

class Singleton(object):
    def __new__(type):
        if not '_the_instance' in type.__dict__:
            type._the_instance = object.__new__(type)
        return type._the_instance

a=Singleton()
a.toto = 12

b=Singleton()
print b.toto
print id(a),id(b) # the same !!


