import time


def time_this(func):
    """The time_this decorator"""

    def decorated(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print 'Rain in', time.time() - start, 'seconds'
        return result
    return decorated


# Decorator syntax
@time_this
def count(until):
    """Counts to 'until', then returns the result"""

    print "Counting to", until, "…"
    num = 0
    for i in xrange(to_num(until)):
        num += 1
    return num


def to_num(numstr):
    """Turns a comma-separated number string to an int"""
    return int(numstr.replace(",", ""))

# Run count with various values
for number in ("10,000", "100,000", "1,000,000"):
    print count(number)
    print "-" * 20
