const int pinT=3;
const int pinF=2;


void setup() {
  Serial.begin(9600);
  pinMode(pinT, OUTPUT);
pinMode(pinF, OUTPUT);
}


void loop() {
  delay(999);
    if(Serial.available() > 0) { // Check if data is available
        String input = Serial.readStringUntil('\n'); // Read string until newline        
        if(input=="T"){
          Serial.print("verde");
          digitalWrite(pinT, HIGH);
          digitalWrite(pinF, LOW);
        }
        else{
          Serial.print("Rosso");
                    digitalWrite(pinF, HIGH);
          digitalWrite(pinT, LOW);
          
        }
      
    }
}
