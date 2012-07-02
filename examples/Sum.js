// ------
// Sum.js
// ------

function assert (b) {
    if (!b) {
        throw "Assertion Error"}}

print("Sum.js\n");

function sum_1 (a) {
    s = 0;
    i = 0;
    while (i != a.length) {
        s += a[i];
        i += 1;}
    return s;}

function sum_2 (a) {
    s = 0;
    for (i = 0; i != a.length; ++i)
        s += a[i];
    return s;}

function sum_3 (a) {
    s = 0;
    for (i in a)
        s += a[i];
    return s;}

function sum_4 (a) {
    s = 0;
    for (p in Iterator(a))
        s += p[1];
    return s;}

function sum_5 (a) {
    s = 0;
    for ([i, v] in Iterator(a))
        s += v;
    return s;}

a = [2, 3, 4];
assert(sum_1(a) == 9);
assert(sum_2(a) == 9);
assert(sum_3(a) == 9);
assert(sum_4(a) == 9);
assert(sum_5(a) == 9);

print("Done.\n");
