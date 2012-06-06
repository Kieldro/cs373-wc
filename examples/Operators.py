#!/usr/bin/env python

# ------------
# Operators.py
# ------------

import operator

print "Operators.py"

i = 2
j = -i
assert i ==  2
assert j == -2
#-i += 1       # SyntaxError: illegal expression for augmented assignment

i = 2
j = 3
#k = (i = j)  # SyntaxError: invalid syntax
i = j
assert i == 3
assert j == 3

i = 2
j = 3
k = i + j     # operator.add(i, j)
assert i == 2
assert j == 3
assert k == 5
#(i + j) += 1 # SyntaxError: illegal expression for augmented assignment

i = 2
j = 3
#k = (i += j) # SyntaxError: invalid syntax
i += j
assert i == 5
assert j == 3

i = 12
j = 10
k = i / j      # integer division
assert i == 12
assert j == 10
assert k ==  1

i = 12
j = 10
i /= j
assert i ==  1
assert j == 10

i = 5.0
j = 2
k = i / j               # floating point division
assert type(k) is float
assert i       == 5.0
assert j       == 2
assert k       == 2.5

i = 5.0
j = 2
i /= j
assert i == 2.5
assert j == 2

i = 5.0
j = 2
k = i // j              # truncating division
assert type(k) is float
assert i       == 5.0
assert j       == 2
assert k       == 2.0

i = 5.0
j = 2
i //= j
assert i == 2.0
assert j == 2

i = 12
j = 10
k = i % j      # integer mod
assert i == 12
assert j == 10
assert k ==  2

i = 12
j = 10
i %= j
assert i ==  2
assert j == 10

i = 2
j = 3
k = i ** j    # exponentiation
assert i == 2
assert j == 3
assert k == 8

i = 2
j = 3
i **= j
assert i == 8
assert j == 3

i = 2
j = 3
k = i << j     # bit shift left
assert i ==  2
assert j ==  3
assert k == 16

i = 2
j = 3
i <<= j
assert i == 16
assert j ==  3

i = 10          # 0000 0000 0000 1010
j = ~i          # 1111 1111 1111 0101: bit complement
k = ~i + 1      # 1111 1111 1111 0110
assert i ==  10
assert j == -11
assert k == -10

i = 10         # 1010
j = 12         # 1100
k = i & j      # 1000: bit and
assert i == 10
assert j == 12
assert k ==  8

i = 10
j = 12
i &= j
assert i ==  8
assert j == 12

i = 10         # 1010
j = 12         # 1100
k = i | j      # 1110: bit or
assert i == 10
assert j == 12
assert k == 14

i = 10
j = 12
i |= j
assert i == 14
assert j == 12

i = 10         # 1010
j = 12         # 1100
k = i ^ j      # 0110: bit exclusive or
assert i == 10
assert j == 12
assert k ==  6

i = 10
j = 12
i ^= j
assert i ==  6
assert j == 12

i = 10         # 1010
j = 12         # 1100
i ^= j
assert i ==  6 # 0110
assert j == 12 # 1100
j ^= i
assert i ==  6 # 0110
assert j == 10 # 1010
i ^= j
assert i == 12 # 1100
assert j == 10 # 1010

i = 10
j = 12
i += j
assert i == 22
assert j == 12
j = i - j
assert i == 22
assert j == 10
i -= j
assert i == 12
assert j == 10

i = 3
j = 5
k = 7
l = 8
assert (i < j) and (j < k) and (k < l)
assert (i < j < k < l)

a = True
b = True
c = False
assert a and b
assert not (a and c)
assert a or b
assert a or c
assert (a and b) == (not (not a or not b))
assert (a and c) == (not (not a or not c))

a = [2, 3, 4]
assert a[1] == 3 # list index
a[1] += 1
assert a[1] == 4

assert [2, 3, 4][1] == 3 # list index
[2, 3, 4][1] += 1        # ?

a = (2, 3, 4)
assert a[1] == 3 # tuple index
#a[1] += 1       # TypeError: 'tuple' object does not support item assignment

s = "a"
t = "bc"
u = s + t             # string concatenation
assert u is not "abc"
assert u ==     "abc"

a = [2]
b = [3, 4]
c = a + b             # list concatenation
assert c == [2, 3, 4]
assert c != (2, 3, 4)

a = (2,)
b = (3, 4)
c = a + b             # tuple concatenation
assert c == (2, 3, 4)
assert c != [2, 3, 4]

print "Done."
