#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

void setup() {
lcd.begin(16, 2); 

}

void loop() {
lcd.print("GreenHackerTeam"); 
lcd.setCursor(0, 1);
lcd.print("Unity IS Power");
delay(5000);
lcd.clear();
lcd.print("We are together ");
lcd.setCursor(0, 1);
lcd.print("WinHtut");
delay(5000);
lcd.clear();

}
