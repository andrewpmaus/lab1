/*
  Blink
  Turns on an LED on for one second, then off for one second, repeatedly.
 
  This example code is in the public domain.
 */
 
 //paste look-up table here from References in ES432 folder

#define LED_R 6
#define LED_G 5
#define LED_B 3

int val;
// the setup routine runs once when you press reset:
void setup() {                
  Serial.begin(9600); //Open Serial Port
}

// the loop routine runs over and over again forever:
void loop() {
  val = analogRead(A0);
  Serial.print("The pot is: ");
  Serial.println(val);
  analogWrite(LED_R, val/4);   // turn the LED on (HIGH is the voltage level)               // wait for a second
}
