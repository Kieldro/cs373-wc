// ------------
// Operators.js
// ------------

function assert (b) {
    if (!b) {
        throw "Assertion Error";}}

print("Operators.js\n");

i = 2;
j = -i;          // negation
assert(i ==  2);
assert(j == -2);
//++-i;          // error: Invalid increment operand

i = 2;
j = ++i;        // pre-increment
assert(i == 3);
assert(j == 3);
//++++i;        // error: Invalid increment operand

i = 2;
j = i++;        // post-increment
assert(i == 3);
assert(j == 2);
//i++++;        // error: Invalid increment operand

i = 2;
j = 3;
k = (i = j);
assert(i == 3);
assert(j == 3);
assert(k == 3);
//++(i = j);    // error: Invalid increment operand

i = 2;
j = 3;
k = i + j;      // addition
assert(i == 2);
assert(j == 3);
assert(k == 5);
//++(i + j);    // error: Invalid increment operand

i = 2;
j = 3;
k = (i += j);
assert(i == 5);
assert(j == 3);
assert(k == 5);
//++(i += j);   // error: Invalid increment operand

i = 12;
j = 10;
k = i / j;         // division
assert(i == 12);
assert(j == 10);
assert(k ==  1.2);
//++(i / j);       // error: Invalid increment operand

i = 12;
j = 10;
k = (i /= j);
assert(i ==  1.2);
assert(j == 10);
assert(k ==  1.2);
//++(i /= j);      // error: Invalid increment operand

i = 12;
j = 10;
k = i % j;       // mod
assert(i == 12);
assert(j == 10);
assert(k ==  2);
//++(i % j);     // error: Invalid increment operand

i = 12;
j = 10;
k = i %= j;
assert(i ==  2);
assert(j == 10);
assert(k ==  2);
//++(i %= j);    // error: Invalid increment operand

i = 2;
j = 3;
k = i << j;      // bit shift left
assert(i ==  2);
assert(j ==  3);
assert(k == 16);
//++(i << j);    // error: Invalid increment operand

i = 2;
j = 3;
k = i <<= j;
assert(i == 16);
assert(j ==  3);
assert(k == 16);
//++(i <<= j);   // error: Invalid increment operand

i = 10;           // 0000 0000 0000 1010
j = ~i;           // 1111 1111 1111 0101: bit complement
k = ~i + 1;       // 1111 1111 1111 0110
assert(i ==  10);
assert(j == -11);
assert(k == -10);

i = 10;          // 1010
j = 12;          // 1100
k = i & j;       // 1000: bit and
assert(i == 10);
assert(j == 12);
assert(k ==  8);

i = 10;
j = 12;
k = (i &= j);
assert(i ==  8);
assert(j == 12);
assert(k ==  8);

i = 10;          // 1010
j = 12;          // 1100
k = i | j;       // 1110: bit or
assert(i == 10);
assert(j == 12);
assert(k == 14);

i = 10;
j = 12;
k = (i |= j);
assert(i == 14);
assert(j == 12);
assert(k == 14);

i = 10;          // 1010
j = 12;          // 1100
k = i ^ j;       // 0110: bit exclusive or
assert(i == 10);
assert(j == 12);
assert(k ==  6);

i = 10;
j = 12;
k = (i ^= j);
assert(i ==  6);
assert(j == 12);
assert(k ==  6);

i = 10;          // 1010
j = 12;          // 1100
i ^= j;
assert(i ==  6); // 0110
assert(j == 12); // 1100
j ^= i;
assert(i ==  6); // 0110
assert(j == 10); // 1010
i ^= j;
assert(i == 12); // 1100
assert(j == 10); // 1010

i = 10;
j = 12;
i += j;
assert(i == 22);
assert(j == 12);
j = i - j;
assert(i == 22);
assert(j == 10);
i -= j;
assert(i == 12);
assert(j == 10);

a = true;
b = true;
c = false;
assert(a && b);
assert(!(a && c));
assert(a || b);
assert(a || c);
assert((a && b) == !(!a || !b));
assert((a && c) == !(!a || !c));

a = [2, 3, 4];
assert(a[1] == 3); // array index
++a[1];
assert(a[1] == 4);

assert([2, 3, 4][1] == 3); // array index
++[2, 3, 4][1];            // ?

s = "a";
t = "bc";
u = s + t;          // string concatenation
assert(u == "abc");

a = [2];
b = [3, 4];
c = a.concat(b);                             // array concatenation
assert(c != [2, 3, 4]);
assert(!((c < [2, 3, 4]) || (c > [2, 3, 4])));

print("Done.\n");
