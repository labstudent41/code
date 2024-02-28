import java.util.*;
public class TreeMaps {
	public static void main(String args[]) {
		Map<Integer, String> map = new TreeMap<Integer, String>();
		map.put(100, "David");
		map.put(102, "Ravi");
		map.put(101, "Vikas");
		map.put(103, "Utkarsh");
		System.out.println(map);
	
		System.out.println("Before removal");
		for (Map.Entry m: map.entrySet()) {
			System.out.println(m.getKey() + " " + m.getValue());
		}
		
		map.remove(102);
		System.out.println("After removal");
		for (Map.Entry m: map.entrySet()) {
			System.out.println(m.getKey() + " " + m.getValue());
		}
	}
}