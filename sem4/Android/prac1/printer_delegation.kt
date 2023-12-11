interface Printer {
	fun print()
}

class LaserPrinter : Printer by RealPrinter()

class RealPrinter: Printer {
	override fun print() {
		println("Print with a real printer")
	}
}

fun main() {
	val laserP = LaserPrinter()
	laserP.print()
}
