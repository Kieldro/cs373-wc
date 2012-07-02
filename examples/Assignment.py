#!/usr/bin/env python

# -------------
# Assignment.py
# -------------

print "Assignment.py"

#i = (j = 2)  # SyntaxError: invalid syntax
#(i = j) = 2  # SyntaxError: invalid syntax

t = (2, 3)
assert type(t) is tuple
assert t       == (2, 3)

t = 2, 3
assert type(t) is tuple
assert t       == (2, 3)

#i, j = 2       # TypeError: 'int' object is not iterable
#i, j = 2, 3, 4 # ValueError: too many values to unpack
i, j  = 2, 3
assert i == 2
assert j == 3

#i, j = "a"     # ValueError: need more than 1 value to unpack
#i, j = "abc"   # ValueError: too many values to unpack
i, j = "ab"     # a string
assert i == "a"
assert j == "b"

#i, j = (2,)      # ValueError: need more than 1 value to unpack
#i, j = (2, 3, 4) # ValueError: too many values to unpack
i, j  = (2, 3)    # a tuple
assert i == 2
assert j == 3

#i, j = [2]       # ValueError: need more than 1 value to unpack
#i, j = [2, 3, 4] # ValueError: too many values to unpack
i, j  = [2, 3]    # a list
assert i == 2
assert j == 3

#i, j = set([2])       # ValueError: need more than 1 value to unpack
#i, j = set([2, 3, 4]) # ValueError: too many values to unpack
i, j  = set([2, 3])    # a set
assert i == 2
assert j == 3

#i, j = {2 : "abc"}                       # ValueError: need more than 1 value to unpack
#i, j = {2 : "abc", 3 : "def", 4 : "ghi"} # ValueError: too many values to unpack
i, j  = {2 : "abc", 3 : "def"}            # a dict
assert i == 2
assert j == 3

#(i, j) = 2       # TypeError: 'int' object is not iterable
#(i, j) = 2, 3, 4 # ValueError: too many values to unpack
(i, j)  = 2, 3
assert i == 2
assert j == 3

#(i, j) = "a"     # ValueError: need more than 1 value to unpack
#(i, j) = "abc"   # ValueError: too many values to unpack
(i, j) = "ab"     # a string
assert i == "a"
assert j == "b"

#(i, j) = (2)       # TypeError: 'int' object is not iterable
#(i, j) = (2, 3, 4) # ValueError: too many values to unpack
(i, j)  = (2, 3)    # a tuple
assert i == 2
assert j == 3

#(i, j) = [2]       # TypeError: 'int' object is not iterable
#(i, j) = [2, 3, 4] # ValueError: too many values to unpack
(i, j)  = [2, 3]    # a list
assert i == 2
assert j == 3

#(i, j) = set([2])       # ValueError: need more than 1 value to unpack
#(i, j) = set([2, 3, 4]) # ValueError: too many values to unpack
(i, j)  = set([2, 3])    # a set
assert i == 2
assert j == 3

#(i, j) = {2 : "abc"}                       # ValueError: need more than 1 value to unpack
#(i, j) = {2 : "abc", 3 : "def", 4 : "ghi"} # ValueError: too many values to unpack
(i, j)  = {2 : "abc", 3 : "def"}            # a dict
assert i == 2
assert j == 3

#[i, j] = 2       # TypeError: 'int' object is not iterable
#[i, j] = 2, 3, 4 # ValueError: too many values to unpack
[i, j]  = 2, 3
assert i == 2
assert j == 3

#[i, j] = "a"     # ValueError: need more than 1 value to unpack
#[i, j] = "abc"   # ValueError: too many values to unpack
[i, j] = "ab"     # a string
assert i == "a"
assert j == "b"

#[i, j] = (2)       # TypeError: 'int' object is not iterable
#[i, j] = (2, 3, 4) # ValueError: too many values to unpack
[i, j]  = (2, 3)    # a tuple
assert i == 2
assert j == 3

#[i, j] = [2]       # TypeError: 'int' object is not iterable
#[i, j] = [2, 3, 4] # ValueError: too many values to unpack
[i, j]  = [2, 3]    # a list
assert i == 2
assert j == 3

#[i, j] = set([2])       # ValueError: need more than 1 value to unpack
#[i, j] = set([2, 3, 4]) # ValueError: too many values to unpack
[i, j]  = set([2, 3])    # a set
assert i == 2
assert j == 3

#[i, j] = {2 : "abc"}                       # ValueError: need more than 1 value to unpack
#[i, j] = {2 : "abc", 3 : "def", 4 : "ghi"} # ValueError: too many values to unpack
[i, j]  = {2 : "abc", 3 : "def"}            # a dict
assert i == 2
assert j == 3

i = j = k = 2
assert i == 2
assert j == 2
assert k == 2

(i, j) = k = [l, m] = 2, 3
assert i == 2
assert j == 3
assert k == (2, 3)
assert l == 2
assert m == 3

i = 2
j = 3
i, j = j, i   # swap
assert i == 3
assert j == 2

print "Done."
