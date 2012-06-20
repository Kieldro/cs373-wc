// -------------
// Variables.js
// -------------

function assert (b) {
    if (!b) {
        throw "Assertion Error";}}

print("Variables.js\n");

i = 2;
v = i;
assert(i == v);
v += 1;
assert(i == 2);
assert(v == 3);

a = [2, 3, 4];
b = a;
assert(a == b);
a[1] += 1;
assert(a[1] == 4);
assert(b[1] == 4);

a = [2, 3, 4];
b = [2, 3, 4];
assert(a != b);
assert(!(a < b) || (a > b));

a = [2, 3, 4];
b = a;
assert(a == b);
a.push(5);
assert(a == b);
assert(a != [2, 3, 4, 5])
assert(!((a < [2, 3, 4, 5]) || (a > [2, 3, 4, 5])));

print("Done.\n");
