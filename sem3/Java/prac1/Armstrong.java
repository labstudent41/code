import java.util.Scanner;

class Armstrong {
	static Scanner sc = new Scanner(System.in);
	public static void main(String arg[]) {
		System.out.print("Enter an integer : ");
		int num = sc.nextInt();
		int n = num;
		int sum = 0;

		while (n != 0) {
			sum += (int) Math.pow(n % 10, 3);
			n = n / 10;
		}

		System.out.println("Sum of cube of individual digits: " + sum);

		if (sum == num) {
			System.out.println(num + " is an armstrong number");
		} else {
			System.out.println(num + " is not an armstrong number");
		}

	}
}
