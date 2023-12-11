class FileProcessor {
	val data: String by lazy {
		readFile()
	}
	private fun readFile(): String {
		return "Reading data from file ..."
	}
}
fun main() {
	val fileProcessor = FileProcessor()
	println(fileProcessor.data)
}
