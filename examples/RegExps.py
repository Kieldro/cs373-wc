#!/usr/bin/env python

# ----------
# RegExps.py
# ----------

import re

print "RegExps.py"

s = "b ab\naab 123"
a = re.split("ab", s)
assert type(a) == list
assert a       == ['b ', '\na', ' 123']

s = "b ab\naab 123"
a = re.split("ba", s)
assert type(a) == list
assert a       == [s]

s = "b ab\naab 123"
a = re.split("^b", s)                  # start of string
assert type(a) == list
assert a       == ['', ' ab\naab 123']

s = "b ab\naab 123"
a = re.split("^a", s)  # start of string
assert type(a) == list
assert a       == [s]

s = "b ab\naab 123"
r = re.compile("^a", re.M)                         # multiline
assert str(type(r)) == "<type '_sre.SRE_Pattern'>"
a = r.split(s)
assert type(a)      == list
assert a            == ['b ab\n', 'ab 123']

s = "b ab\naab 123"
a = re.split("3$", s)                  # end of string
assert type(a) == list
assert a       == ['b ab\naab 12', '']

s = "b ab\naab 123"
a = re.split("b$", s)  # end of string
assert type(a) == list
assert a       == [s]

s = "b ab\naab 123"
r = re.compile("b$", re.M)                         # multiline
assert str(type(r)) == "<type '_sre.SRE_Pattern'>"
a = r.split(s)
assert type(a)      == list
assert a            == ['b a', '\naab 123']

s = "b ab\naab 123"
a = re.split(".", s)                                                 # any character
assert type(a) == list
assert a       == ['', '', '', '', '\n', '', '', '', '', '', '', '']

s = "b ab\naab 123"
a = re.split("\d", s)                        # any digit
assert type(a) == list
assert a       == ['b ab\naab ', '', '', '']

s = "b ab\naab 123"
a = re.split("\D", s)                                         # any non-digit
assert type(a) == list
assert a       == ['', '', '', '', '', '', '', '', '', '123']

s = "b ab\naab 123"
a = re.split("\w", s)                                          # any alphanumeric
assert type(a) == list
assert a       == ['', ' ', '', '\n', '', '', ' ', '', '', '']

s = "b ab\naab 123"
a = re.split("\W", s)                       # any non-alphanumeric
assert type(a) == list
assert a       == ['b', 'ab', 'aab', '123']

s = "b ab\naab 123"
m = re.search("(a*)b([^a]*)(a*)b", s)            # * is zero or more
assert str(type(m)) == "<type '_sre.SRE_Match'>"
assert m.group(0) == "b ab"
assert m.group(1) == ""
assert m.group(2) == " "
assert m.group(3) == "a"

s = "b ab\naab 123"
m = re.search("(a+)b([^a]*)(a+)b", s)            # + is one or more
assert str(type(m)) == "<type '_sre.SRE_Match'>"
assert m.group(0) == "ab\naab"
assert m.group(1) == "a"
assert m.group(2) == "\n"
assert m.group(3) == "aa"

s = "b ab\naab 123"
m = re.search("(a?)b([^a]*)(a?)b", s)            # ? is zero or one
assert str(type(m)) == "<type '_sre.SRE_Match'>"
assert m.group(0) == "b ab"
assert m.group(1) == ""
assert m.group(2) == " "
assert m.group(3) == "a"

s = "b ab\naab 123"
t = re.sub("b ", "xx", s)
assert s == "b ab\naab 123"
assert t == "xxab\naaxx123"

s = "b ab\naab 123"
t = re.sub("b.", "xx", s)
assert s == "b ab\naab 123"
assert t == "xxab\naaxx123"

s = "b ab\naab 123"
t = re.sub("", "z", s)
assert s == "b ab\naab 123"
assert t == "zbz zazbz\nzazazbz z1z2z3z"

print "Done."
