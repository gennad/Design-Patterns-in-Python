Python

The desired properties of the Singleton pattern can most simply be encapsulated in Python by defining a module, containing module-level variables and functions. To use this modular Singleton, client code merely imports the module to access its attributes and functions in the normal manner. This sidesteps many of the wrinkles in the explicitly-coded versions below, and has the singular advantage of requiring zero lines of code to implement.

According to influential Python programmer Alex Martelli, The Singleton design pattern (DP) has a catchy name, but the wrong focus—on identity rather than on state. The Borg design pattern has all instances share state instead.[5] A rough consensus in the Python community is that sharing state among instances is more elegant, at least in Python, than is caching creation of identical instances on class initialization. Coding shared state is nearly transparent:

class Borg:
   __shared_state = {}
   def __init__(self):
       self.__dict__ = self.__shared_state
   # and whatever else is needed in the class -- that's all!

But with the new style class, this is a better solution, because only one instance is created:

class Singleton (object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'self'):
            cls.self = object.__new__(cls)
        return cls.self

#Usage
mySingleton1 = Singleton()
mySingleton2 = Singleton()

#mySingleton1 and  mySingleton2 are the same instance.
assert mySingleton1 is mySingleton2

Two caveats:

    The __init__-method is called every time Singleton() is called, unless cls.__init__ is set to an empty function.
    If it is needed to inherit from the Singleton-class, instance should probably be a dictionary belonging explicitly to the Singleton-class.

class  InheritableSingleton (object):
    instances = {}
    def __new__(cls, *args, **kwargs):
        if InheritableSingleton.instances.get(cls) is None:
            cls.__original_init__ = cls.__init__
            InheritableSingleton.instances[cls] = object.__new__(cls, *args, **kwargs)
        elif cls.__init__ == cls.__original_init__:
            def nothing(*args, **kwargs):
                pass
            cls.__init__ = nothing
        return InheritableSingleton.instances[cls]

To create a singleton that inherits from a non-singleton, multiple inheritance must be used.

class  Singleton (NonSingletonClass, object):
    instance = None
    def __new__(cls, *args, **kargs):
        if cls.instance is None:
            cls.instance = object.__new__(cls, *args, **kargs)
        return cls.instance

Be sure to call the NonSingletonClass's __init__ function from the Singleton's __init__ function.

A more elegant approach using metaclasses was also suggested.[6]

class SingletonType(type):
    def __call__(cls):
        if getattr(cls, '__instance__', None) is None:
            instance = cls.__new__(cls)
            instance.__init__()
            cls.__instance__ = instance
        return cls.__instance__

# Usage
class Singleton(object):
    __metaclass__ = SingletonType

    def __init__(self):
        print '__init__:', self

class OtherSingleton(object):
    __metaclass__ = SingletonType

    def __init__(self):
        print 'OtherSingleton __init__:', self

# Tests
s1 = Singleton()
s2 = Singleton()
assert s1
assert s2
assert s1 is s2

os1 = OtherSingleton()
os2 = OtherSingleton()
assert os1
assert os2
assert os1 is os2


