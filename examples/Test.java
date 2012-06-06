// ----------
// Hello.java
// ----------

class X {}

class A extends X {}

class B extends X {}

final class Test {
    public static void main (String[] args) {
        System.out.println("Test.java");

        assert(new B() == new A());

        System.out.println("Done.");}}
