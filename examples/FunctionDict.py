#!/usr/bin/env python

# ---------------
# FunctionDict.py
# ---------------

def f (x, y, **z) :
    assert type(z) is dict
    return [x, y, z]

print "FunctionDict.py"

assert f(2, 3)               == [2, 3, {}]
assert f(2, 3, a = 4)        == [2, 3, {'a' : 4}]
assert f(2, 3, a = 4, b = 5) == [2, 3, {'a' : 4, 'b' : 5}]
assert f(2, 3, a = 4, b = 5) == [2, 3, {'b' : 5, 'a' : 4}]

d = {"b" : 4, "a" : 3}
assert d            == {'b' : 4, 'a' : 3}
assert d            == {'a' : 3, 'b' : 4}
assert f(2, 5, **d) == [2, 5, {'a' : 3, 'b' : 4}]
assert f(2, 5, **d) == [2, 5, {'b' : 4, 'a' : 3}]

d = {"a" : 3, "b" : 4, "c" : 5}
#assert f(2, **d) == [{"a" : 3, "b" : 4, "c" : 5}] # TypeError: f() takes exactly 2 non-keyword arguments (1 given)

d = {"a" : 3, "b" : 4, "y" : 5}
assert f(2, **d) == [2, 5, {'a': 3, 'b' : 4}]
assert f(2, **d) == [2, 5, {'b': 4, 'a' : 3}]

d = {"a" : 3, "x" : 4, "y" : 5}
#assert f(2, **d) == [2, 5, {'a': 3, 'x' : 4}] # TypeError: f() got multiple values for keyword argument 'x'
assert  f(**d)    == [4, 5, {'a': 3}]

print "Done."
