import abc


class ComponentInterface(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def component_function(self):
        pass


class Leaf(ComponentInterface):
    def __init__(self, number):
        self.number = number

    def component_function(self):
        print("i'm leaf number: {}".format(self.number))


class Composite(ComponentInterface):
    def __init__(self):
        self._children = set()

    def append_child(self, child):
        self._children.add(child)

    def remove_child(self, child):
        self._children.remove(child)

    def component_function(self):
        for child in self._children:
            child.component_function()


if __name__ == '__main__':
    composite = Composite()
    for number in range(2):
        composite.append_child(Leaf(number))
    composite.component_function()
