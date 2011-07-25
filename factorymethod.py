class A(object):
    def __init__(self):
        self.a = "Hello"

class B(object):
    def __init__(self):
        self.a = " World"
        myfactory = {
        "greeting" : A,
        "subject" : B,
        }

>>> print myfactory["greeting"]().a
Hello

