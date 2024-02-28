// import java.util.Scanner;

class Strings {
	public static void main(String args[]) {
		// Scanner sc = new Scanner(System.in);

		String s = new String("Hello");
		System.out.println(s.length());

		StringBuffer sb = new StringBuffer("Hello");
		System.out.println(sb.length());
		sb.setLength(0);

		System.out.println("Finished!");
	}
}
