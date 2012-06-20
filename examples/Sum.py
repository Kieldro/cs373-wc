#!/usr/bin/env python

# ------
# Sum.py
# ------

import operator

def sum_1 (a) :
    s = 0
    i = 0
    while i != len(a) :
        s += a[i]
        i += 1
    return s

def sum_2 (a) :
    s = 0
    for i in range(len(a)) :
        s += a[i]
    return s

def sum_3 (a) :
    s = 0
    for i in xrange(len(a)) :
        s += a[i]
    return s

def sum_4 (a) :
    s = 0
    p = iter(a)
    while True :
        try :
            s += p.next()
        except StopIteration :
            break
    return s

def sum_5 (a) :
    s = 0
    for v in a :
        s += v
    return s

def sum_6 (a) :
    return reduce(operator.add, a, 0)

print "Sum.py"

a = [2, 3, 4]
assert sum_1(a) == 9
assert sum_2(a) == 9
assert sum_3(a) == 9
assert sum_4(a) == 9
assert sum_5(a) == 9
assert sum_6(a) == 9
assert   sum(a) == 9

a = (2, 3, 4)
assert sum_1(a) == 9
assert sum_2(a) == 9
assert sum_3(a) == 9
assert sum_4(a) == 9
assert sum_5(a) == 9
assert sum_6(a) == 9
assert   sum(a) == 9

x = set([2, 3, 4])
# assert sum_1(x) == 9 # TypeError: 'set' object does not support indexing
# assert sum_2(x) == 9 # TypeError: 'set' object does not support indexing
# assert sum_3(x) == 9 # TypeError: 'set' object does not support indexing
assert sum_4(a) == 9
assert sum_5(a) == 9
assert sum_6(a) == 9
assert   sum(x) == 9

print "Done."
