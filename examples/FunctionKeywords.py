#!/usr/bin/env python

# -------------------
# FunctionKeywords.py
# -------------------

def f (x, y, z) :
    return [x, y, z]

print "FunctionKeywords.py"

assert f(2, 3, 4)         == [2, 3, 4]
assert f(2, z = 4, y = 3) == [2, 3, 4]

print "Done."
