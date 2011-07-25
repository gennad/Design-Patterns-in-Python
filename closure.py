def Dx(f, dx):
    def dfdx(x):
        return (f(x + dx) - f(x))/dx
    return dfdx

def f(x):
    return 3*x**2+x

"""
>>> print f(1.0)
4.0
>>> print Dx(f, 0.01)(1.0)
7.03
>>> print Dx(Dx(f, 0.01), 0.01)(1.0)
"""
