#include<Servo.h>
Servo myServe;
int analog=0;
void setup() {
 pinMode(analog,INPUT);
 myServe.attach(9);
 Serial.begin(9600);
}

void loop() {
 int a_data=analogRead(analog);
 int degree=map(a_data,0,1023,0,179);
 myServe.write(degree);
 delay(10); 

}
