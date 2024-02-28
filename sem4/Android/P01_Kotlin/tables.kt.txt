fun main() {
	println("Enter a number")
	var num = readLine()!!.toInt()
	for (i in 1..10) {
		println("$num x $i = " + (num * i))
	}
}
