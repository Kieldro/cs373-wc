// ------------
// Iteration.js
// ------------

function assert (b) {
    if (!b) {
        throw "Assertion Error"}}

print("Iteration.js\n");

i = 0;
s = 0;
while (i != 10) {
    s += i;
    ++i;}
assert(i == 10);
assert(s == 45);

i = 0;
s = 0;
do {
    s += i;
    ++i;}
while (i != 10);
assert(i == 10);
assert(s == 45);

s = 0;
for (i = 0; i != 10; ++i)
    s += i;
assert(i == 10);
assert(s == 45);

a = [2, 3, 4];
b = [5, 6, 7];
s = 0;
for (i = 0, j = 0; i != 3; ++i, ++j)
    s += a[i] + b[j];
assert(s == 27);

a = [2, 3, 4];
s = 0;
for (i in a)
    s += parseInt(i);
assert(s == 3);

a = [2, 3, 4];
s = 0;
for (p in Iterator(a))
    s += p[0]
assert(s == 3);

a = [2, 3, 4];
s = 0;
for (p in Iterator(a))
    p[1] += 1
assert(!((a < [2, 3, 4]) || (a > [2, 3, 4])));

print("Done.\n");
