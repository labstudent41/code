import java.util.HashSet;
class Sets {
	public static void main(String args[]) {
        HashSet<Integer> set = new HashSet<Integer>();
        for (int i = 0; i < 5; i++) {
			set.add(i);
        }
		set.set(4, 5);
		System.out.println("List current length" + set.size());
	}
}
