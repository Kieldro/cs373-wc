#!/usr/bin/env python

# ------------
# Iteration.py
# ------------

import itertools

print "Iteration.py"

a = [2, 3, 4]
for v in a :
    v += 1            # ?
assert a == [2, 3, 4]

a = ["abc", "def", "ghi"]
for v in a :
    v += "x"              # ?
assert a == ["abc", "def", "ghi"]

a = [[2], [3], [4]]
for v in a :
    v += [5]                         # ?
assert a == [[2, 5], [3, 5], [4, 5]]

a = [(2,), (3,), (4,)]
for v in a :
    v += (5,)                  # ?
assert a == [(2,), (3,), (4,)]

a = [(2, "abc"), (3, "def"), (4, "ghi")]
s = 0
for u, v in a :
    s += u
assert s == 9

d = {2 : "abc", 3 : "def", 4 : "ghi"}
s = 0
for k in d :
    s += k
assert s == 9

d = {2 : "abc", 3 : "def", 4 : "ghi"}
s = 0
for k, v in d.items() :
    s += k
assert s == 9

x = range(0, 10)
assert type(x) is list
assert x       == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

x = xrange(0, 10)
assert type(x) is xrange
assert x       != [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert x[0] == 0
assert x[9] == 9
try :
    assert x[10] == 10                           # error: out of range
    assert False
except IndexError :
    pass
#x[0] = 2                                        # TypeError: 'xrange' object does not support item assignment
s = 0
for v in x :
    s += v
assert s == 45

x = xrange(0, 15)
s = 0
for v in x :
    if v == 10 :
        break
    s += v
else :                                           # else clause in a for loop
    assert False                                 # executes when the loop terminates normally
assert s == 45

x = itertools.count(0)
assert type(x) is itertools.count
#assert x[0] == 0                 # TypeError: 'itertools.count' object is unsubscriptable
s = 0
for v in x :
    if v == 10 :
        break
    s += v
assert s == 45

x = [2, 3, 4, 5, 6]
y = []
assert type(y) is list
for v in x :
    y.append(v * 5)
assert x == [ 2,  3,  4,  5,  6]
assert y == [10, 15, 20, 25, 30]

x = [2, 3, 4, 5, 6]
y = [v * 5 for v in x]                 # list comprehension
assert type(y) is list
assert x       == [2,   3,  4,  5,  6]
assert y       == [10, 15, 20, 25, 30]

x = [2, 3, 4, 5, 6]
y = []
for v in x :
    if v % 2 :
        y.append(v * 5)
assert x == [2, 3, 4, 5, 6]
assert y == [15, 25]

x = [2, 3, 4, 5, 6]
y = [v * 5 for v in x if v % 2]
assert x == [2, 3, 4, 5, 6]
assert y == [15, 25]

x = [2, 3, 4]
y = [4, 5]
z = []
for v in x :
    for w in y :
        z.append(v + w)
assert x == [2, 3, 4]
assert y == [4, 5]
assert z == [2+4, 2+5, 3+4, 3+5, 4+4, 4+5]
assert z == [6, 7, 7, 8, 8, 9]

x = [2, 3, 4]
y = [4, 5]
z = [v + w for v in x for w in y]
assert x == [2, 3, 4]
assert y == [4, 5]
assert z == [2+4, 2+5, 3+4, 3+5, 4+4, 4+5]
assert z == [6, 7, 7, 8, 8, 9]

print "Done."
