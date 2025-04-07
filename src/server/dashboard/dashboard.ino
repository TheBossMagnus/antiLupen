<<<<<<< HEAD
const int pinT=3;
const int pinF=2;

=======
//const int ledPins[3][3] = {
//    {3, 4, 5}, // LED  0
//    {6, 7, 8}, // LED  1
//    {9, 10, 11} // LED  2
//};

const int ledPins[2][3] = {
    {3, 5, 6}, // LED 0
    {9, 10, 11} // LED 1
};
>>>>>>> b375a65aca514e9a8745b2291d13484c208378cf

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
