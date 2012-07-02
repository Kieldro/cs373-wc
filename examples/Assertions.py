#!/usr/bin/env python

# -------------
# Assertions.py
# -------------

"""
Turn OFF assertions at run time with -O.
% python -O Assertions.py
"""

def cycle_length (n) :
    assert n > 0
    c = 0
    while n > 1 :
        if (n % 2) == 0 :
            n = (n / 2)
        else :
            n = (3 * n) + 1
        c += 1
    assert c > 0
    return c

print "Assertions.py"

assert cycle_length(1) == 1
assert cycle_length(5) == 6

print "Done."

"""
Assertions.py
Traceback (most recent call last):
  File "./Assertions.py", line 26, in <module>
    assert cycle_length(1) == 1
  File "./Assertions.py", line 21, in cycle_length
    assert c > 0
AssertionError
"""
