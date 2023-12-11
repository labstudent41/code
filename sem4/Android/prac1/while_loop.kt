fun main() {
	var n = 4
	var fact = 1
	var i = 1
	do {
		fact = fact * i
		i++
	} while (i <= n)
	print("factorial is $fact")
}
