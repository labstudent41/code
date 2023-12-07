import java.util.Scanner;

class Prime_no_test {
	public static void main(String arg[]) {
		Scanner sc = new Scanner(System.in);
		System.out.print("Enter a number : ");
		int n = sc.nextInt();

		int found = 0;
		for (int i = 2; i < (n/2)+1; i++) {
			if (n % i == 0) {
				found = 1;
				break;
			}
		}
		if (found == 0) {
			System.out.println(n + " is a prime number");
		} else {
			System.out.println(n + " is not a prime number");
		}
	}
}
