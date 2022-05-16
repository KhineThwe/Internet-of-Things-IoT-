void setup() {
  pinMode(2,OUTPUT);
  pinMode(3,OUTPUT);
  Serial.begin(9600);
  Serial.println("Welcome to our serial communication!!");

}

void loop() {
  // put your main code here, to run repeatedly:
int data=0;
if(Serial.available()){
  data=Serial.read();
  Serial.println(data);
  if(data==49){
    digitalWrite(2,HIGH);
    digitalWrite(3,HIGH);
    delay(5000);
    Serial.println("LED is on");
    digitalWrite(2,LOW);
    digitalWrite(3,LOW);
    delay(5000);
    Serial.println("LED is off");
  }else{
    digitalWrite(2,LOW);
    digitalWrite(3,LOW);
    Serial.println("LED is off");
  }
}
}
