#!/usr/bin/env python

print "Test.py"
print

i = 2147483647
print type(i)
print "i =", i
print

i += 1
print type(i)
print "i =", i
print

print "Done."

"""
Test.py

<type 'int'>
i = 2147483647

<type 'long'>
i = 2147483648

Done.
"""
