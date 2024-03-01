int time = 300;

void setup() {
  pinMode(8,OUTPUT);
  pinMode(9,OUTPUT);
  pinMode(10, OUTPUT);
}

void loop() {
  digitalWrite(8,HIGH);
  delay(time);
  digitalWrite(8,LOW);
  delay(time);
  digitalWrite(9,HIGH);
  delay(time);
  digitalWrite(9,LOW);
  delay(time);
  digitalWrite(10, HIGH);
  delay(time);
  digitalWrite(10, LOW);
  delay(time);
}
