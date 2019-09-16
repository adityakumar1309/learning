## String vs StringBuffer vs StringBuilder

String is immutable whereas StringBuffer and StringBuider are mutable classes.

StringBuffer is thread safe and synchronized whereas StringBuilder is not, thats why StringBuilder is more faster than StringBuffer.

String concat + operator internally uses StringBuffer or StringBuilder class.

For String manipulations in non-multi threaded environment, we should use StringBuilder else use StringBuffer class.

## String in Java

String class represents character strings, we can instantiate String by two ways.

String str = "abc"; or String str = new String ("abc");

String is immutable in Java, so it’s easy to share it across different threads or functions.

When we create a String using double quotes, it first looks for the String with the same value in the JVM string pool, if found it returns the reference else it creates the String object and then places it in the String pool. This way JVM saves a lot of space by using the same String in different threads. But if a new operator is used, it explicitly creates a new String in the heap memory.
