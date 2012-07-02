#!/usr/bin/env python

"""
CS373: Quiz #7 (9 pts)
"""

""" ----------------------------------------------------------------------
1. In the paper, "A Bug and a Crash" about the Ariane 5, what was the
   software bug?
   (2 pts)

the conversion of a 64-bit number to a 16-bit number
"""

""" ----------------------------------------------------------------------
2. In the paper, "Mariner 1", what was the software bug?
   (1 pt)

the ommission of a hyphen
"""

""" ----------------------------------------------------------------------
3. What is the output of the following program?
   (2 pts)

True
False
"""

a = [2, 3, 4]
b = a
b += [5]
print a is b

a = (2, 3, 4)
b = a
b += (5,)
print a is b

""" ----------------------------------------------------------------------
4. What semantic difference is there between Java's conditional expression
   and Python's? Why?
   (4 pts)

Java's then and else clause must be of the same type
Java is typed and the compiler must be able to determine the type of the
entire conditional expression
"""
