
const int pinT = 3;
const int pinF = 2;

void setup() {
  Serial.begin(9600);
  pinMode(pinT, OUTPUT);
  pinMode(pinF, OUTPUT);
  Serial.print("verde");
  digitalWrite(pinT, HIGH);
  digitalWrite(pinF, LOW);
}


void loop() {
  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n');
    if (input == "T") {
      Serial.print("verde");
      digitalWrite(pinT, HIGH);
      digitalWrite(pinF, LOW);
    }
    else {
      Serial.print("Rosso");
      digitalWrite(pinF, HIGH);
      digitalWrite(pinT, LOW);

    }

  }
}
