#!/usr/bin/env python

# -------------------
# FunctionParallel.py
# -------------------

def f ((x, y), z) :
    return [x, y, z]

#def g ([x, y], z) :  # SyntaxError: invalid syntax
#    return [x, y, z]

print "FunctionParallel.py"

#f(2, 3, 4)                                      # TypeError: f() takes exactly 1 argument (3 given)
#f((2,), 3)                                      # ValueError: need more than 2 values to unpack
#f((2, 3, 4), 5)                                 # ValueError: too many values to unpack
assert f((2, 3), 4)                 == [2, 3, 4]
assert f([2, 3], 4)                 == [2, 3, 4]
assert f(set([2, 3]), 4)            == [2, 3, 4]
assert f({2 : "abc", 3 : "def"}, 4) == [2, 3, 4]
assert f(xrange(2, 4), 4)           == [2, 3, 4]

print "Done."
