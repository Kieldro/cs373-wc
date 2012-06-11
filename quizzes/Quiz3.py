#!/usr/bin/env python

"""
CS373: Quiz #3 (9 pts)
"""

""" ----------------------------------------------------------------------
1. What are the four elements of the Circle of Life?
   [XP: Ch.2, Pg. 16]
   (4 pts)

define, estimate, choose, build
"""

""" ----------------------------------------------------------------------
2. In pair programming which of the partners should do most of the
   driving?
   [XP: Ch. 12, Pg. 90]
   (2 pts)

the one who is least sure of what's being done
"""

""" ----------------------------------------------------------------------
3. Given positive integers, b and e, let m = e / 2. If b <= m, then
   max_cycle_length(b, e) = max_cycle_length(m, e). True or False?
   [Collatz]
   (3 pts)

True

Consider b = 10, e = 100.
Then m = 50.
max_cycle_length(10, 100) = max_cycle_length(50, 100)
All the numbers between 10 and 50 can be mapped to numbers between 50 and
and 100 by one or more doublings, so none of those numbers could have a
larger cycle length.
"""
