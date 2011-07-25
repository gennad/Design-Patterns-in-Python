def bisection(line):
    return 5.5, 6.6

def conjugate_gradient(line):
    return 3.3, 4.4

def test():
    solver = conjugate_gradient
    print solver((5.5,5.5))
    solver = bisection
    print solver((5.5,5.5))
test()

