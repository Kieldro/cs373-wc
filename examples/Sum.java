// --------
// Sum.java
// --------

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.HashSet;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.ListIterator;
import java.util.TreeSet;

final class Sum {
    public static int sum_1 (int[] a) {
        int s = 0;
        for (int i = 0; i != a.length; ++i)
            s += a[i];
        return s;}

    public static int sum_2 (int[] a) {
        int s = 0;
        for (int v : a)
            s += v;
        return s;}

    public static int sum_3 (List<Integer> x) {
        int s = 0;
        for (int i = 0; i != x.size(); ++i)
            s += x.get(i);
        return s;}

    public static int sum_4 (List<Integer> x) {
        int s = 0;
        for (ListIterator<Integer> p = x.listIterator(); p.hasNext();)
            s += p.next();
        return s;}

    public static int sum_5 (Collection<Integer> x) {
        int s = 0;
        for (Iterator<Integer> p = x.iterator(); p.hasNext();)
            s += p.next();
        return s;}

    public static int sum_6 (Collection<Integer> x) {
        int s = 0;
        for (int v : x)
            s += v;
        return s;}

    public static void main (String[] args) {
        System.out.println("Sum.java");

        {
        final int[] a = {2, 3, 4};
        assert(sum_1(a) == 9);
        assert(sum_2(a) == 9);
        }

        {
        final Integer[] a = {2, 3, 4};

        {
        List<Integer> x = Arrays.asList(a);
        assert(sum_3(x) == 9);
        assert(sum_4(x) == 9);
        assert(sum_5(x) == 9);
        assert(sum_6(x) == 9);
        }

        {
        final ArrayList<Integer> x = new ArrayList<Integer>(Arrays.asList(a));
        assert(sum_3(x) == 9);
        assert(sum_4(x) == 9);
        assert(sum_5(x) == 9);
        assert(sum_6(x) == 9);
        }

        {
        final LinkedList<Integer> x = new LinkedList<Integer>(Arrays.asList(a));
        assert(sum_3(x) == 9);
        assert(sum_4(x) == 9);
        assert(sum_5(x) == 9);
        assert(sum_6(x) == 9);
        }

        {
        final TreeSet<Integer> x = new TreeSet<Integer>(Arrays.asList(a));
//      assert(sum_3(x) == 9);
//      assert(sum_4(x) == 9);
        assert(sum_5(x) == 9);
        assert(sum_6(x) == 9);
        }

        {
        final HashSet<Integer> x = new HashSet<Integer>(Arrays.asList(a));
//      assert(sum_3(x) == 9);/
//      assert(sum_4(x) == 9);
        assert(sum_5(x) == 9);
        assert(sum_6(x) == 9);
        }
        }

        System.out.println("Done.");}}
