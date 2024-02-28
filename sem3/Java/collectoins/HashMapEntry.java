import java.util.*;
public class HashMapEntry {
	public static void main(String args[]) {
		Map<Integer, String> map = new HashMap<Integer, String>();
		map.put(1, "David");
		map.put(2, "Ravi");
		map.put(3, "Vikas");
		map.put(3, "Utkarsh");
		
		Set st = map.entrySet();
		Iterator itr = st.iterator();
		while (itr.hasNext()) {
			Map.Entry entry = (Map.Entry)itr.next();
			System.out.println(entry.getKey() + " " + entry.getValue());
		}
	}
}
