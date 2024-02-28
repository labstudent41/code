class Int_to_byte {
	public static void main(String arg[]) {
		byte b = 127;
		for (int i = 1; i < 1000; i++) {
			b = (byte) i;
			System.out.println(i + " " + b);
		}
	}
}
