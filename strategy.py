class StrategyExample:

    def __init__(self, func=None):
        if func:
            self.execute = func

    def execute(self):
        print self


def execute_replacement1():
        print "Strategy 1"


def execute_replacement2():
    print "Strategy 2"

if __name__ == "__main__":

    strat0 = StrategyExample()
    strat1 = StrategyExample(execute_replacement1)
    strat2 = StrategyExample(execute_replacement2)

    strat0.execute()
    strat1.execute()
    strat2.execute()

# -------------------- With classes --------------------

# Interface
class StrategicAlternative(object):
    def the_method(self, some_arg, obj):
        raise NotImplementedError("Must subclass me")

class Strategy(object):
    def __init__(self, the_class):
        self.strategy = the_class

    def do_something(self, some_arg):
        self.strategy.the_method(some_arg, self)


class AlternativeOne(StrategicAlternative):
    def the_method(self, some_arg, obj):
        print self, some_arg


class AlternativeTwo(StrategicAlternative):
    def the_method(self, some_arg, obj):
        print self, some_arg


t = Strategy(AlternativeOne())
t.do_something('Strategy 1')

t = Strategy(AlternativeTwo())
t.do_something('Strategy 2')
