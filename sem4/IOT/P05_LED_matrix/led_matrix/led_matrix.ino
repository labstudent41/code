int rows[8] = { 7, 6, 5, 4, 3, 2, 1, 0 };
int cols[8] = { 19, 18, 17, 16, 15, 14, 9, 8 };

void setup() {
  for (int i = 0; i < 8; i++) {
    pinMode(rows[i], OUTPUT);
    pinMode(cols[i], OUTPUT);
    digitalWrite(cols[i], HIGH);
  }
}

void draw(int matrix[8][8]) {
	for (int x = 0; x < 3000; x++) {
		for (int i = 0; i < 8; i++) {
			digitalWrite(rows[i], HIGH);
			for (int j = 0; j < 8; j++) {
				digitalWrite(cols[j], matrix[i][j]);
				digitalWrite(cols[j], HIGH);
			}
			digitalWrite(rows[i], LOW);
		}
	}

  for (int i = 0; i < 8; i++) {
    digitalWrite(rows[i], LOW);
    digitalWrite(cols[i], HIGH);
  }
}

int A[8][8] = {
  { 1, 1, 1, 1, 1, 1, 1, 1 },
  { 1, 1, 1, 0, 0, 1, 1, 1 },
  { 1, 1, 0, 1, 1, 0, 1, 1 },
  { 1, 1, 0, 1, 1, 0, 1, 1 },
  { 1, 1, 0, 0, 0, 0, 1, 1 },
  { 1, 1, 0, 1, 1, 0, 1, 1 },
  { 1, 1, 0, 1, 1, 0, 1, 1 },
  { 1, 1, 1, 1, 1, 1, 1, 1 },
};

void loop() {
  digitalWrite(LED_BUILTIN, HIGH);
  draw(A);
  digitalWrite(LED_BUILTIN, LOW);
  delay(1000);
}
