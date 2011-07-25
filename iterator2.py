# from a sequence
x = [42, "test", -12.34]
it = iter(x)
try:
  while True:
    x = next(it) # in Python 2, you would use it.next()
    print x
except StopIteration:
  pass

# a generator
def foo(n):
  for i in range(n):
    yield i

it = foo(5)
try:
  while True:
    x = next(it) # in Python 2, you would use it.next()
    print x
except StopIteration:
  pass
