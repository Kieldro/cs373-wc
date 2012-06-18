// ----------
// Cache.java
// ----------

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

final class Cache {
    public static void main (String[] args) {
        System.out.println("Cache.java");

        {
        int i = 2;
        int j = 2;
        assert i == j;
        ++i;
        assert i != j;
        ++j;
        assert i == j;
        }

        {
        Integer x = new Integer(2);
        Integer y = new Integer(2);
        assert x            != y;
        assert x.intValue() == y.intValue();
        ++x;
        assert x            != y;
        assert x.intValue() != y.intValue();
        ++y;
        assert x            == y;
        assert x.intValue() == y.intValue();
        }

        {
        Integer x = 2;
        Integer y = 2;
        assert x == y;
        ++x;
        assert x != y;
        }

        {
        Integer x = 128; // cache: [-128, 127]
        Integer y = 128;
        assert x != y;
        --x;
        --y;
        assert x == y;
        }

        {
        Long x = 128L;
        Long y = 128L;
        assert x != y;
        --x;
        --y;
        assert x == y;
        }

        {
        int  i = 2;
//      Long x = 2;        // doesn't compile
        Long x = (long) i;
        }

        {
        long    j = 2;
//      Integer x = j;       // doesn't compile
        Integer x = (int) j;
        }

        {
        int[]     a = {2, 3, 4};
//      Integer[] b = a;         // doesn't compile
        Integer[] b = {2, 3, 4};
        }

        {
        String s = "abc";
        String t = "abc";
        assert s == t;
        }

        {
        String s = "abc";
        String t = "ab" + "c";
        assert s == t;
        }

        {
        String s = "abc";
        String u = "ab";
        String v = "c";
        String t = u + v;
        assert s != t;
        assert s.equals(t);
        }

        System.out.println("Done.");}}
