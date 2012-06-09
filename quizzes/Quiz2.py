#!/usr/bin/env python

"""
CS373: Quiz #2 (9 pts)
"""

""" ----------------------------------------------------------------------
1. Which of the following is true? Maybe more than one.
   [Collatz]
   (3 pts)

a. (n / 2),  with n even, always produces an even
b. (n / 2),  with n even, always produces an odd
c. (3n + 1), with n odd,  always produces an even
d. (3n + 1), with n odd,  always produces an odd

c.
"""

"""
CS373: Quiz #2 (10 pts)
"""

""" ----------------------------------------------------------------------
2. What is the output of the following program?
   [Collatz]
   (3 pts)

5
11
"""

def f (n) :
    return n + (n >> 1) + 1

print f(3)
print f(7)

""" ----------------------------------------------------------------------
3. In the context of Project #1: Collatz, what is f() computing?
   [Collatz]
   (3 pts)

For odd n it's computing (3n + 1) / 2.
(3n + 1) / 2
3n/2 + 1/2
n + n/2 + 1/2
n + n/2 + 1, because n is odd
n + (n >> 1) + 1
"""
