import java.util.Scanner;

class Palindrome {
	public static void main(String arg[]) {
		Scanner sc = new Scanner(System.in);
		System.out.print("Enter text : ");
		String text = sc.next();
		String reverse = "";

		for (int i = 0; i < text.length(); i++) {
			reverse = text.charAt(i) + reverse;
		}

		System.out.println("Reverse is : " + reverse);

		if (text.equals(reverse)) {
			System.out.println("Given text is a palindrome.");
		} else {
			System.out.println("Given text is not a palindrome.");
		}
	}
}
