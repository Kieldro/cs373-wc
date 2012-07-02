#!/usr/bin/env python

# -------------
# Exceptions.py
# -------------

def f (b) :
    if b :
        raise NameError("abc")
    return 0

print "Exceptions.py"

try :
    assert f(False) == 0
except NameError :
    assert False

try :
    assert f(True) == 0
    assert False
except NameError, e :
    assert type(e)      is     NameError
    assert type(e.args) is     tuple
    assert len(e.args)  is     1
    assert e.args       is not ("abc",)
    assert e.args       ==     ("abc",)

assert issubclass(NameError,     Exception)
assert issubclass(Exception,     BaseException)
assert issubclass(NameError,     BaseException)
assert issubclass(BaseException, object)

print "Done."
