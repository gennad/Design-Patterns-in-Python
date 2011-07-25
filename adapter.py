class Barfooer:
    def barfoo(self, bar, foo):
        pass

# Per instance, by wrapping and delegation
class FoobaringWrapper:
    def __init__(self, wrappee):
        self.w = wrappee
    def foobar(self, foo, bar):
        return self.w.barfoo(bar, foo)

foobarer = FoobaringWrapper(barfooer)

# Per-classs by subclassing and self-delegation
class Foobarer(Barfooer):
    def foobar(self,foo, bar):
        return self.barfoo(bar, foo)

foobarer = Foobarer(some, init, params)

