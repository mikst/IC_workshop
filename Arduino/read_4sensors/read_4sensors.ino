int val[4];
int pin[]={A0, A1, A2, A3};

void setup() {
Serial.begin(9600);
pinMode(13,OUTPUT);
// pin 13 provides 5V to the sensors
digitalWrite(13,HIGH);
}

void loop() {
 // Serial.print("[ ");
for (int i=0; i<4; i++){
  val[i] = analogRead(pin[i]);
  Serial.print(val[i]);
  Serial.print(" ");
}
Serial.println();
delay(100);
}
