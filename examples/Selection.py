#!/usr/bin/env python

# ------------
# Selection.py
# ------------

def f (n) :
    if n < 0 :
        m = -1
    elif n > 0 :
        m = 1
    else :
        m = 0
    return m

def g (n) :
    return -1 if (n < 0) else (1 if (n > 0) else 0)

print "Selection.py"

assert f(-2) == -1
assert f( 0) ==  0
assert f( 3) ==  1

assert g(-2) == -1
assert g( 0) ==  0
assert g( 3) ==  1

print "Done."
