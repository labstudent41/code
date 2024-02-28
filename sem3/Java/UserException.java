// Custom exception class
class CustomException extends Exception {
	public CustomException(String message) {
		super(message);
	}
}

public class UserException {
	// Method that simulates a custom exception condition
	static void checkAge(int age) throws CustomException {
		if (age < 18) {
			throw new CustomException("Age must be 18 or older.");
		}
		System.out.println("You are eligible.");
	}

	public static void main(String[] args) {
		try {
			int userAge = 15; // Replace with the age you want to test

			// Call the method that may raise the custom exception
			checkAge(userAge);

			// If the checkAge method doesn't throw an exception, this line will be reached.
			System.out.println("End of program.");
		} catch (CustomException e) {
			// Handle the custom exception
			System.err.println("CustomException: " + e.getMessage());
		}
	}
}
