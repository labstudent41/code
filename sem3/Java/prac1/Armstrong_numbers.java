import java.util.Scanner;

class Main {
	public static void main(String arg[]) {

		for (int i = 1; i < 1000; i++) {
			int num = i;
			int n = num;
			int sum = 0;

			while (n != 0) {
				sum += Math.pow(n % 10, 3);
				n = n / 10;
			}

			if (sum == num) {
				System.out.println(num + " is an armstrong number");
			}
		}

	}
}
