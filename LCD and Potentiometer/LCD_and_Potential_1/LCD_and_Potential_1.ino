#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
int ldr=0;
int led=6;
void setup() {
lcd.begin(16, 2); 
pinMode(ldr,INPUT);
pinMode(led,OUTPUT);
Serial.begin(9600);
}

void loop() {
int ldr_data=analogRead(ldr);
lcd.print(ldr_data); 
Serial.println(ldr_data);
int led_data=analogRead(led);
Serial.println(led_data);
analogWrite(led,led_data/4);
lcd.setCursor(0, 1);
lcd.print("Unity IS Power");
delay(1000);
lcd.clear();
lcd.print("We are together ");
lcd.setCursor(0, 1);
lcd.print("WinHtut");
delay(1000);
lcd.clear();

}
