import java.util.Scanner

class Car(var brand: String, var year: Int)

fun main() {
	var scanner = Scanner(System.`in`)
	print("Enter Brand: ")
	var brand = scanner.next()
	print("Enter Year: ")
	var year = scanner.nextInt()
	var c2 = Car(brand, year)
	println(c2.brand + " manufactured in " + c2.year)
}
