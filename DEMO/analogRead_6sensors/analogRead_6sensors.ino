int val1;
int val2;
int val3;
int val4;
int val5;
int val6;

int avg1;
int avg2;
int avg3;
int avg4;
int avg5;
int avg6;

int samplesize = 8; // avarage sample size

void setup() {
  // start serial communication
  Serial.begin(9600);

  // load avarage with initial value
  avg1 = analogRead(A0);
  avg2 = analogRead(A1);
  avg3 = analogRead(A2);
  avg4 = analogRead(A3);
  avg5 = analogRead(A4);
  avg6 = analogRead(A5);
}

void loop() {

  // read all the sensor pins
  val1 = analogRead(A0);
  val2 = analogRead(A1);
  val3 = analogRead(A2);
  val4 = analogRead(A3);
  val5 = analogRead(A4);
  val6 = analogRead(A5);

// smooth with taking avarage
  avg1 = (avg1*(samplesize-1) + val1)/samplesize;
  val1=avg1;
  avg2 = (avg2*(samplesize-1) + val2)/samplesize;
  val2=avg2;
  avg3 = (avg3*(samplesize-1) + val3)/samplesize;
  val3=avg3;
  avg4 = (avg4*(samplesize-1) + val4)/samplesize;
  val4=avg4;
  avg5 = (avg5*(samplesize-1) + val5)/samplesize;
  val5=avg5;
  avg6 = (avg6*(samplesize-1) + val6)/samplesize;
  val6=avg6;

// print to serial
  Serial.print(val1);
  Serial.print(" ");
  Serial.print(val2);
  Serial.print(" ");
  Serial.print(val3);
  Serial.print(" ");
  Serial.print(val4);
  Serial.print(" ");
  Serial.print(val5);
  Serial.print(" ");
  Serial.print(val6);
  Serial.print(" ");
  Serial.print(1023); // max value to fix the plotter range
  Serial.print(" ");
  Serial.print(0);    // min value to fix the plotter range
  Serial.print(" ");
  Serial.println();   // end of the message

// loop delay, reduce the delay to read sensors more frequently
  delay(50);

}
