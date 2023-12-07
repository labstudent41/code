import java.util.*;
public class HashMaps {
	public static void main(String args[]) {
		Map<Integer, String> m1 = new HashMap<Integer, String>();
		Map<Integer, String> m2 = new HashMap<Integer, String>();
		m1.put(1, "Welcome");
		m1.put(3, "SYCS");
		m1.put(2, "Vartak");
		m2.put(1, "Hello");
		m2.put(3, "Samsung");
		m2.put(2, "J2");
		System.out.println(m1 + " " + m2);
	}
}
	