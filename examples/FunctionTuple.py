#!/usr/bin/env python

# ----------------
# FunctionTuple.py
# ----------------

def f (x, y, *z) :
    assert type(z) is tuple
    return [x, y, z]

print "FunctionTuple.py"

assert f(2, 3)       == [2, 3, ()]
assert f(2, 3, 4)    == [2, 3, (4,)]
assert f(2, 3, 4, 5) == [2, 3, (4, 5)]

t = (3, 4)
assert t           == (3, 4)
assert t           != (4, 3)
assert f(2, t,  5) == [2, (3, 4), (5,)]
assert f(2, 5,  t) == [2, 5, ((3, 4),)]
assert f(2, 5, *t) == [2, 5, (3, 4)]

l = [3, 4]
assert l           == [3, 4]
assert l           != [4, 3]
assert f(2, l,  5) == [2, [3, 4], (5,)]
assert f(2, 5,  l) == [2, 5, ([3, 4],)]
assert f(2, 5, *l) == [2, 5, (3, 4)]

s = set([4, 3])
assert s           == set([4, 3])
assert s           == set([3, 4])
assert f(2, s,  5) == [2, set([3, 4]), (5,)]
assert f(2, 5,  s) == [2, 5, (set([3, 4]),)]
assert f(2, 5, *s) == [2, 5, (3, 4)]

d = {"b" : 4, "a" : 3}
assert d                    == {'b' : 4, 'a' : 3}
assert d                    == {'a' : 3, 'b' : 4}
assert f(2, d,  5)          == [2, {'a' : 3, 'b' : 4}, (5,)]
assert f(2, 5,  d)          == [2, 5, ({'a' : 3, 'b' : 4},)]
assert f(2, 5, *d.keys())   == [2, 5, ('a', 'b')]
assert f(2, 5, *d.values()) == [2, 5, (3, 4)]
assert f(2, 5, *d.items())  == [2, 5, (('a', 3), ('b', 4))]
assert f(2, 5, *d)          == [2, 5, ('a', 'b')]
#assert f(**d)              == [4, 5, ()]                    # TypeError: f() got an unexpected keyword argument 'a'

d = {"y" : 4, "x" : 3}
assert f(**d) == [3, 4, ()]

d = {"y" : 4, "x" : 3, "a" : 5}
#assert f(**d) == [3, 4, ("a",)] # TypeError: f() got an unexpected keyword argument 'a'

d = {"x" : 3}
#assert f(2, **d) == [3, 4, ()] # TypeError: f() got multiple values for keyword argument 'x'

d = {"y" : 4}
assert f(2, **d) == [2, 4, ()]

print "Done."
