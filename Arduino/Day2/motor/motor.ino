int analog=0;

void setup() {
  pinMode(analog,INPUT);
  pinMode(led,OUTPUT);
  Serial.begin(9600);

}

void loop() {
int a_data=analogRead(analog);
Serial.println(a_data);
analogWrite(led,a_data/4);
}
