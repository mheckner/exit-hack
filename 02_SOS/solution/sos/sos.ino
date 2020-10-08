/*
  Blink
  Lights an LED, when a button is pressed.
  Use this example as a starting point for SOS.
*/

int LED_PIN = 12;
int BUTTON_PIN = 2;

// the setup function runs once when you press reset or power the board
void setup() {
  pinMode(LED_PIN, OUTPUT);
  pinMode(BUTTON_PIN, INPUT);
}

// the loop function runs over and over again forever
void loop() {
  if (digitalRead(BUTTON_PIN) == HIGH) {
    digitalWrite(LED_PIN, HIGH);
  } else {
    digitalWrite(LED_PIN, LOW);
  }
}
