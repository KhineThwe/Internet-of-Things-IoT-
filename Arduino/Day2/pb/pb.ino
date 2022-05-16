int pb=2;
int led=6;
void setup() {
  pinMode(pb,INPUT);
  pinMode(led,OUTPUT);
  Serial.begin(9600);
  Serial.println("Welcome to our serial communication!!");

}

void loop() {

int pData = digitalRead(pb);
if(pData==HIGH){
  digitalWrite(led,HIGH);
  //delay(5000);
}else{
  digitalWrite(led,LOW);
 // delay(5000);
}


}
