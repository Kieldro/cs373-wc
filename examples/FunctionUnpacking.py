#!/usr/bin/env python

# --------------------
# FunctionUnpacking.py
# --------------------


def f (x, y, z) :
    return [x, y, z]

print "FunctionUnpacking.py"

assert f(2, 3, 4)     == [2, 3, 4]
#assert f(2, 3)       == None)     # TypeError: f() takes exactly 3 arguments (2 given
#assert f(2, 3, 4, 5) == None)     # TypeError: f() takes exactly 3 arguments (4 given

t = (3, 4)
s = (2, 3, 4)
assert t            == (3, 4)
assert t            != (4, 3)
assert f(2, t, 5)   == [2, (3, 4), 5]
assert f(2, 5, t)   == [2, 5, (3, 4)]
assert f(2, *t)     == [2, 3, 4]
#f(*t, 2)                              # SyntaxError: invalid syntax
#f(*t)                                 # TypeError: f() takes exactly 3 arguments (2 given)
#f(2, 5, *t)                           # TypeError: f() takes exactly 3 arguments (4 given)
assert f(*s)        == [2, 3, 4]
#f(5, *s)                              # TypeError: f() takes exactly 3 arguments (4 given)

l = [3, 4]
assert l            == [3, 4]
assert l            != [4, 3]
assert f(2, l, 5)   == [2, [3, 4], 5]
assert f(2, 5, l)   == [2, 5, [3, 4]]
assert f(2, *l)     == [2, 3, 4]
#f(*l, 2)                             # SyntaxError: only named arguments may follow *expression
#f(*l)                                # TypeError: f() takes exactly 3 arguments (2 given)
#f(2, 5, *l)                          # TypeError: f() takes exactly 3 arguments (4 given)

s = set([4, 3])
assert s            == set([4, 3])
assert s            == set([3, 4])
assert f(2, s, 5)   == [2, set([3, 4]), 5]
assert f(2, 5, s)   == [2, 5, set([3, 4])]
assert f(2, *s)     == [2, 3, 4]
#f(*s, 2)                                  # SyntaxError: only named arguments may follow *expression
#f(*s)                                     # TypeError: f() takes exactly 3 arguments (2 given)
#f(2, 5, *s)                               # TypeError: f() takes exactly 3 arguments (4 given)

d = {"b" : 4, "a" : 3}
assert d                  == {'b' : 4, 'a' : 3}
assert d                  == {'a' : 3, 'b' : 4}
assert f(2, d, 5)         == [2, {'a' : 3, 'b' : 4}, 5]
assert f(2, 5, d)         == [2, 5, {'a' : 3, 'b' : 4}]
assert (type(d.keys()))   is list
assert f(2, *d.keys())    == [2, 'a', 'b']
assert (type(d.values())) is list
assert f(2, *d.values())  == [2, 3, 4]
assert (type(d.items()))  is list
assert f(2, *d.items())   == [2, ('a', 3), ('b', 4)]
assert f(2, *d)           == [2, 'a', 'b']
#f(2, **d)                                              # TypeError: f() got an unexpected keyword argument 'a'

d = {"z" : 4, "y" : 3}
assert f(2, **d) == [2, 3, 4]
#f(**d)                       # TypeError: f() takes exactly 3 arguments (2 given)
#f(**d, 2)                    # SyntaxError: invalid syntax

d = {"z" : 4, "y" : 3, "a" : 2}
#f(2, **d)                      # TypeError: f() got an unexpected keyword argument 'a'

d = {"z" : 4, "y" : 3, "x" : 2}
#f(2, **d)                      # TypeError: f() got multiple values for keyword argument 'x'

print "Done."
