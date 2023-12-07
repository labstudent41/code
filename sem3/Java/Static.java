
import java.util.Scanner;

class Computer {
	static String company;
	static String factory_location;
	static {
		System.out.println("=== Computer Class loaded");
		factory_location = "China";
	}
	String model;
	String type;
	Computer(String company, String model, String type) {
		System.out.println("=== Computer Object created");
		this.company = company;
		this.model = model;
		this.type = type;
	}
	void show_details() {
		System.out.println(company + " " + model + " " + type);
	}
	static String get_company() {
		return (company + " " + factory_location);
	}
}

class Static {
	public static void main(String arg[]) {
		System.out.println("=== Main started...");
		Computer rn7 = new Computer("Redmi", "Note 7", "Smart Phone");
		Computer rn9 = new Computer("Redmi", "Note 9", "Smart Phone");
		rn7.company = "MI";
		System.out.println(rn7.company);
		System.out.println(rn7.get_company());
		rn7.show_details();
		rn9.show_details();
	}
}
