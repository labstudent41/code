class InvalidAge extends Exception {
	InvalidAge() {
		System.out.println("Age can only be a positive integer");
	}
}

class InvalidAgeRelation extends Exception {
	InvalidAgeRelation() {
		System.out.println("Father's age cannot be less than Son's");
	}
}

class Father {
	int age;
	void setAge(int age) {
		try {
			if (age < 0) {
				throw new InvalidAge();
			}
			this.age = age;
		} catch (InvalidAge e) {}
	}
}

class Son extends Father {
	int age;
	void setAge(Father father, int age) {
		try {
			if (father.age < age) {
				throw new InvalidAgeRelation();
			}
			this.age = age;
		} catch (InvalidAgeRelation e) {}
	}
}

class FatherSon {
	public static void main(String args[]) {
		Father father = new Father();
		father.setAge(45);
		Son son = new Son();
		son.setAge(father, 20);
	}
}
