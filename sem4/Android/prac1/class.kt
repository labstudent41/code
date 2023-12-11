class Car {
	var brand: String = ""
	var year: Int = 0
}

class Bike (
	var brand: String,
	var year: Int
)

fun main() {
	var c1 = Car()
	c1.brand = "Bugatti"
	c1.year = 1987
	println(c1.brand + " manufactured in " + c1.year)

	var c2 = Car()
	c2.brand = "Toyota"
	c2.year = 2000
	println(c2.brand + " manufactured in " + c2.year)

	var b1 = Bike("Honda", 2005)
	println(b1.brand + " manufactured in " + b1.year)
}
