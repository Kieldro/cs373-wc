#!/usr/bin/env python

# -------
# Sets.py
# -------

print "Sets.py"

s = set([2, 3.45, "abc", 2])
assert type(s) is     set
assert len(s)  ==     3
assert s       ==     set([2, 3.45, 'abc'])
assert s       is not set([2, 3.45, 'abc'])
assert s       ==     set((2, 'abc', 3.45))
assert s       ==     frozenset((2, 3.45, 'abc'))

s = frozenset([2, 3.45, "abc", 2])
assert type(s)      is     frozenset
assert len(s)       ==     3
assert s            ==     frozenset([2, 3.45, 'abc'])
assert s            is not frozenset([2, 3.45, 'abc'])
assert s            ==     frozenset((2, 'abc', 3.45))
assert s            ==     set((2, 3.45, 'abc'))

s = set({2 : "ghi", 3.45 : 3, "abc" : 6.78, 2 : "def"})
assert type(s) is set
assert s       == set([2, 3.45, "abc"])

s = frozenset({2 : "ghi", 3.45 : 3, "abc" : 6.78, 2 : "def"})
assert type(s) is frozenset
assert s       == frozenset([2, 3.45, "abc"])

set()       ==     set()
set()       is not set()
frozenset() is     frozenset()

s = set([2, 3.45, "abc", 2])
t = set(s)
assert s ==     t
assert s is not t

s = frozenset([2, 3.45, "abc", 2])
t = frozenset(s)
assert s is t

s = set([2, 3.45, "abc"])
t = s.copy()
assert s ==     t
assert s is not t

s = frozenset([2, 3.45, "abc"])
t = s.copy()
assert s is t

s = set([2, 3.45, "abc"])
t = s
assert s is t
s |= frozenset([6])
assert s == set([2, 3.45, "abc", 6])
assert s is t

s = frozenset([2, 3.45, "abc"])
t = s
assert s is t
s |= frozenset([6])
assert s == frozenset([2, 3.45, "abc", 6])
assert t == frozenset([2, 3.45, "abc"])

s = set()
s.add(2)
s.add(3.45)
s.add("abc")
s.add(2)
assert s == set([2, 3.45, "abc"])
s.remove("abc")
assert s == set([2, 3.45])
try :
    s.remove("abc")
    assert False
except KeyError, e:
    assert type(e.args) is tuple
    assert len(e.args)  == 1
    assert e.args       == ("abc",)

s = frozenset([2, 3.45, "abc"])
assert 2     in s
assert 3 not in s

s = frozenset([1, 3])
t = frozenset([1, 3, 5, 7])
assert s <  t               # proper subset
assert s <= t
assert t >  s               # proper superset
assert t >= s

s = frozenset([1, 2, 3, 5])
t = frozenset([1, 2, 4, 6])
assert (s | t) == frozenset([1, 2, 3, 4, 5, 6]) # union
assert (t | s) == frozenset([1, 2, 3, 4, 5, 6])
assert (s & t) == frozenset([1, 2])             # intersection
assert (t & s) == frozenset([1, 2])
assert (s - t) == frozenset([3, 5])             # difference
assert (t - s) == frozenset([4, 6])
assert (s ^ t) == frozenset([3, 5, 4, 6])       # symmetric difference
assert (t ^ s) == frozenset([3, 5, 4, 6])

assert False is not 0
assert False ==     0
assert True  is not 1
assert True  ==     1
assert 2     is not 2L
assert 2     ==     2L
s = set((False, 0, True, 1, 2, 2L))
assert s == set((False, True, 2))
assert s == set((0, 1, 2L))

class A (object) :
    pass

assert A() != A()
s = set([A(), A()])
assert len(s) == 2

s = set(["abc",             "def"])
s = set([(2, 3),            (4, 5)])
s = set([frozenset([2, 3]), frozenset([4, 5])])

#s = set([set([2, 3]), set([4, 5])]) # TypeError: set objects are unhashable
#s = set([[2, 3],      [4, 5]])      # TypeError: list objects are unhashable

print "Done."
