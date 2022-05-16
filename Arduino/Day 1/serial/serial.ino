void setup(){
  Serial.begin(9600);
}
void loop(){
  int data=0;
  if(Serial.available()){
    data = Serial.read();
    Serial.println(data);
    if(data==49){
      Serial.println("User entered data is 1");
    }else{
      Serial.println("User entered another data");
    }
    }
}
