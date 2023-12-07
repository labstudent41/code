class Animal {
	String name;

	Animal(String name) {
		this.name = name;
	}

	void speak() {
		System.out.println(name + " makes a sound");
	}
}

// Child class inheriting from Animal
class Dog extends Animal {
	Dog(String name) {
		super(name); // Call the constructor of the parent class
	}

	// Method overriding: Override the speak method of the parent class
	@Override
	void speak() {
		System.out.println(name + " barks");
	}
}

// Child class inheriting from Animal
class Cat extends Animal {
	Cat(String name) {
		super(name); // Call the constructor of the parent class
	}

	// Method overriding: Override the speak method of the parent class
	@Override
	void speak() {
		System.out.println(name + " meows");
	}
}

public class MethodOverriding {
	public static void main(String[] args) {
		// Create instances of Dog and Cat
		Dog dog = new Dog("Buddy");
		Cat cat = new Cat("Whiskers");

		// Call the speak method on Dog and Cat objects
		dog.speak(); // This will invoke the overridden speak method in Dog class
		cat.speak(); // This will invoke the overridden speak method in Cat class
	}
}
