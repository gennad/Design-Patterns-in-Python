## {{{ http://code.activestate.com/recipes/86651/ (r1)
from copy import deepcopy

class Prototype:
    def __init__(self):
        self._objs = {}

    def registerObject(self, name, obj):
        """
        register an object.
        """
        self._objs[name] = obj

    def unregisterObject(self, name):
        """unregister an object"""
        del self._objs[name]

    def clone(self, name, **attr):
        """clone a registered object and add/replace attr"""
        obj = deepcopy(self._objs[name])
        obj.__dict__.update(attr)
        return obj

## end of http://code.activestate.com/recipes/86651/ }}}

