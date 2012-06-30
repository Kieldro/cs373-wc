#!/usr/bin/env python

# -------------------
# FunctionDefaults.py
# -------------------

def f (x, y, z = 4) :
    return [x, y, z]

#def g (x, y = 3, z) : # SyntaxError: non-default argument follows default argument
#    return [x, y, z]

def g (x = 2, y = 3, z = 4) :
    return [x, y, z]

def h1 (x = []) : # mutable default
    x += [2]
    return x

def h2 (x = ()) : # immutable default
    x += (2,)
    return x

def h3 (x = None) :
    if x is None :
        x = []
    x += [2]
    return x

print "FunctionDefaults.py"

assert f(2, 3)    == [2, 3, 4]
assert f(2, 3, 5) == [2, 3, 5]

assert g()         == [2, 3, 4]
assert g(5)        == [5, 3, 4]
assert g(5, 6)     == [5, 6, 4]
assert g(5, 6, 7)  == [5, 6, 7]
assert g(5, z = 7) == [5, 3, 7]
#g(5, x = 6)                    # TypeError: g() got multiple values for keyword argument 'x'

assert h1()    == [2]
assert h1()    == [2, 2]
assert h1([1]) == [1, 2]
assert h1()    == [2, 2, 2]
assert h1([1]) == [1, 2]

assert h2()     == (2,)
assert h2()     == (2,)
assert h2((1,)) == (1, 2)
assert h2()     == (2,)
assert h2((1,)) == (1, 2)

assert h3()    == [2]
assert h3()    == [2]
assert h3([1]) == [1, 2]
assert h3()    == [2]
assert h3([1]) == [1, 2]

print "Done."
