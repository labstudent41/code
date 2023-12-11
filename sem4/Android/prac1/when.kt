fun main() {
	print("Enter sun, moon or earth : ")
	val planet = readLine()!!
	when (planet) {
		"earth" -> println("You are here")
		"sun" -> println("Never mess with it")
		"moon" -> println("Earth's girlfriend")
		else -> println("What nonsense?")
  }
}
