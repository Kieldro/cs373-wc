#!/usr/bin/env python

# ---------
# Arrays.py
# ---------

def test_1 (T) :
    assert not T()

    a = T("abCbA")
    assert len(a) == 5

    a = T("abCbA")
    assert a[2] == "C"
    try :
        assert a[5] == 0                               # index error
        assert False
    except IndexError, e :
        assert type(e.args)    is tuple
        assert len(e.args)     == 1
        assert e.args[0][-18:] == "index out of range"

    a = T("abCbA")
    assert a[-3] == "C"
    try :
        assert a[-6] == 0                              # index error
        assert False
    except IndexError, e :
        assert type(e.args)    is tuple
        assert len(e.args)     == 1
        assert e.args[0][-18:] == "index out of range"

    a = T("abCbA")
    i = iter(a)
    assert str(type(i))[-10:-2] == "iterator"
    assert i is iter(i)

    a = T("abCbA")
    assert "C"     in a
    assert "d" not in a

    a = T("abCbA")
    assert not (a != a)
    assert     (a == a)
    assert not (a <  a)
    assert     (a <= a)
    assert not (a >  a)
    assert     (a >= a)

    a = T("abCbA")
    assert (a + a) == T("abCbAabCbA")
    b  = T("abCbA")
    b += a
    assert b == T("abCbAabCbA")

    a = T("abCbA")
    assert (3 * a) == T("abCbAabCbAabCbA")
    b  = T("abCbA")
    b *= 3
    assert b == T("abCbAabCbAabCbA")

    a = T("abCbA")
    assert a[1:4] == T("bCb")
    assert a[1: ] == T("bCbA")
    assert a[ :4] == T("abCb")
    assert a[0:5] == T("abCbA")
    assert a[0:6] == T("abCbA")
    assert a[ : ] == T("abCbA")

    a = T("abCbA")
    assert a[ 1: 4: 2] == T("bb")
    assert a[-4:-1: 2] == T("bb")
    assert a[ 0: 5: 2] == T("aCA")
    assert a[-5: 5: 2] == T("aCA")
    assert a[  :  : 2] == T("aCA")

    a = T("abCbA")
    assert a[ 1: 4:-2] == T("")
    assert a[ 3: 0:-2] == T("bb")
    assert a[-2:-5:-2] == T("bb")
    assert a[ 4:-6:-2] == T("ACa")
    assert a[-1:-6:-2] == T("ACa")
    assert a[  :  :-2] == T("ACa")

    a = T("abCbA")
    assert a[ :  :-1] == T("AbCba")
    assert a[4:-6:-1] == T("AbCba")

def test_2 (T) :
    a = T([2, 3, 4])
    assert sum(a, 0) == 9
    assert sum(a)    == 9

    a = T(["abc", "de"])
#   assert sum(a, "") == "abcde"; # TypeError: sum() can't sum strings [use "".join(seq) instead]
    assert "".join(a) == "abcde"

    a = T([[2, 3, 4], [5, 6]])
    assert sum(a, []) == [2, 3, 4, 5, 6]
#   assert sum(a)     == [2, 3, 4, 5, 6] # TypeError: unsupported operand type(s) for +: 'int' and 'list'

    a = T([(2, 3, 4), (5, 6)])
    assert sum(a, ()) == (2, 3, 4, 5, 6)
#   assert sum(a)     == (2, 3, 4, 5, 6) # TypeError: unsupported operand type(s) for +: 'int' and 'tuple'

print "Arrays.py"

test_1(str)
test_1(list)
test_1(tuple)

test_2(list)
test_2(tuple)

print "Done."
