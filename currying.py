# With a class
class Curry(object):
    def __init__(self, f, *a, **k):
        self.f, self.a, self.k = f, a, k
    def __call__(self, *b, **kk):
        d = self.k.copy()
        d.update(kk)
        return self.f(*(b+self.a), **d)

btn.setOnClick(Curry(foo, 23))

# With a closure
def curry(f, *a, **k):
    def curried(*b, **kk):
        d = k.copy()
        d.update(kk)
        return f(*(b+a), **d)
    return curried
btn.setOnClick(curry(foo, 23))

