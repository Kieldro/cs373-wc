#!/usr/bin/env python

"""
CS373: Quiz #11 (9 pts)
"""

""" ----------------------------------------------------------------------
1. What is the multiplicity of an association?
   [Basic UML & SQL: Associations]
   (1 pts)

how many instances of a class are connected to an instance of another
class
"""

""" ----------------------------------------------------------------------
1. What is the output of the following program?
   (4 pts)

[5, 3, 7]
[5, 6, 4]
"""

def f (x = 2, y = 3, z = 4) :
    return [x, y, z]

print f(5, z = 7)
print f(y = 6, x = 5)
