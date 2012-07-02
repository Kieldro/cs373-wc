// --------------
// Iteration.java
// --------------

import java.util.Arrays;

final class Iteration {
    public static void main (String[] args) {
        System.out.println("Iteration.java");

        {
        int i = 0;
        int s = 0;
        while (i != 10) {
            s += i;
            ++i;}
        assert i == 10;
        assert s == 45;
        }

        {
        int i = 0;
        int s = 0;
        do {
            s += i;
            ++i;}
        while (i != 10);
        assert i == 10;
        assert s == 45;
        }

        {
        int s = 0;
        for (int i = 0; i != 10; ++i)
            s += i;
//      assert i == 10;               // error: cannot find symbol
        assert s == 45;
        }

        {
        final int[] a = {2, 3, 4};
        final int[] b = {5, 6, 7};
        int s = 0;
        for (int i = 0, j = 0; i != 3; ++i, ++j)
            s += a[i] + b[j];
        assert s == 27;
        }

        {
        final int[] a = {2, 3, 4};
              int   s = 0;
        for (int v : a)
            ++v;                                     // ?
        assert Arrays.equals(a, new int[]{2, 3, 4});
        }

        {
        final String[] a = {"abc", "def", "ghi"};
              int      s = 0;
        for (String v : a)
            v += "x";                                               // ?
        assert Arrays.equals(a, new String[]{"abc", "def", "ghi"});
        }

        {
        final StringBuilder[] a = {new StringBuilder("abc"), new StringBuilder("def"), new StringBuilder("ghi")};
              int             s = 0;
        for (StringBuilder v : a)
            v.append("x");                                                                                                              // ?
        assert !Arrays.equals(a, new StringBuilder[]{new StringBuilder("abcx"), new StringBuilder("defx"), new StringBuilder("ghix")});
        assert a[0].toString().equals("abcx");
        assert a[1].toString().equals("defx");
        assert a[2].toString().equals("ghix");
        }

        System.out.println("Done.");}}
