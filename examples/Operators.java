// --------------
// Operators.java
// --------------

class Operators {
    public static void main (String[] args) {
        System.out.println("Operators.java");

        {
        int i = 2;
        int j = -i;     // negation
        assert i ==  2;
        assert j == -2;
//      ++-i;           // error: unexpected type
        }

        {
        int i = 2;
        int j = ++i;   // pre-increment
        assert i == 3;
        assert j == 3;
//      ++++i;         // error: unexpected type
        }

        {
        int i = 2;
        int j = i++;   // post-increment
        assert i == 3;
        assert j == 2;
//      i++++;         // error: unexpected type
        }

        {
        int i = 2;
        int j = 3;
        int k = (i = j);
        assert i == 3;
        assert j == 3;
        assert k == 3;
//      ++(i = j);       // error: unexpected type
        }

        {
        int i = 2;
        int j = 3;
        int k = i + j; // addition
        assert i == 2;
        assert j == 3;
        assert k == 5;
//      ++(i + j);     // error: unexpected type
        }

        {
        int i = 2;
        int j = 3;
        int k = (i += j);
        assert i == 5;
        assert j == 3;
        assert k == 5;
//      ++(i += j);       // error: unexpected type
        }

        {
        int i = 12;
        int j = 10;
        int k = i / j;  // integer division
        assert i == 12;
        assert j == 10;
        assert k ==  1;
        }

        {
        int i = 12;
        int j = 10;
        int k = (i /= j);
        assert i ==  1;
        assert j == 10;
        assert k ==  1;
        }

        {
        int i = 12;
        int j = 10;
        int k = i % j;  // integer mod
        assert i == 12;
        assert j == 10;
        assert k ==  2;
        }

        {
        int i = 12;
        int j = 10;
        int k = (i %= j);
        assert i ==  2;
        assert j == 10;
        assert k ==  2;
        }

        {
        int i = 2;
        int j = 3;
        int k = i << j; // bit shift left
        assert i ==  2;
        assert j ==  3;
        assert k == 16;
        }

        {
        int i = 2;
        int j = 3;
        int k = (i <<= j);
        assert i == 16;
        assert j ==  3;
        assert k == 16;
        }

        {
        int i = 10;      // 0000 0000 0000 1010
        int j = ~i;      // 1111 1111 1111 0101: bit complement
        int k = ~i + 1;  // 1111 1111 1111 0110
        assert i ==  10;
        assert j == -11;
        assert k == -10;
        }

        {
        int i = 10;     // 1010
        int j = 12;     // 1100
        int k = i & j;  // 1000: bit and
        assert i == 10;
        assert j == 12;
        assert k ==  8;
        }

        {
        int i = 10;
        int j = 12;
        int k = (i &= j);
        assert i ==  8;
        assert j == 12;
        assert k ==  8;
        }

        {
        int i = 10;     // 1010
        int j = 12;     // 1100
        int k = i | j;  // 1110: bit or
        assert i == 10;
        assert j == 12;
        assert k == 14;
        }

        {
        int i = 10;
        int j = 12;
        int k = (i |= j); // 1110
        assert i == 14;
        assert j == 12;
        assert k == 14;
        }

        {
        int i = 10;     // 1010
        int j = 12;     // 1100
        int k = i ^ j;  // 0110: bit exclusive or
        assert i == 10;
        assert j == 12;
        assert k ==  6;
        }

        {
        int i = 10;
        int j = 12;
        int k = (i ^= j);
        assert i ==  6;
        assert j == 12;
        assert k ==  6;
        }

        {
        int i = 10;     // 1010
        int j = 12;     // 1100
        i ^= j;
        assert i ==  6; // 0110
        assert j == 12; // 1100
        j ^= i;
        assert i ==  6; // 0110
        assert j == 10; // 1010
        i ^= j;
        assert i == 12; // 1100
        assert j == 10; // 1010
        }

        {
        int i = 10;
        int j = 12;
        i += j;
        assert i == 22;
        assert j == 12;
        j = i - j;
        assert i == 22;
        assert j == 10;
        i -= j;
        assert i == 12;
        assert j == 10;
        }

        {
        boolean a = true;
        boolean b = true;
        boolean c = false;
        assert a && b;
        assert !(a && c);
        assert a || b;
        assert a || c;
        assert (a && b) == !(!a || !b);
        assert (a && c) == !(!a || !c);
        }

        {
        int[] a = {2, 3, 4};
        assert a[1] == 3;    // array index
        ++a[1];
        assert a[1] == 4;
        }

        {
        assert new int[]{2, 3, 4}[1] == 3; // array index
        ++new int[]{2, 3, 4}[1];           // ?
        }

        {
        final int[] a = {2, 3, 4};
        assert a[1] == 3;    // array index
        ++a[1];
        assert a[1] == 4;
        }

        {
        String s = "a";
        String t = "bc";
        String u = s + t;       // string concatenation
        assert u != "abc";
        assert u.equals("abc");
        }

        System.out.println("Done.");}}
