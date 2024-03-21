#include <Wire.h>
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27,16,2);       //init LCD screen

void setup() {
  lcd.init();                           // Initialize the LCD with 16 columns and 2 rows
  lcd.backlight();                      // put your setup code here, to run once:
  lcd.clear();                          // Clear the LCD screen
  lcd.setCursor(0, 0);                  // Print
  lcd.print("Type here:");              // Print
  lcd.setCursor(0, 1);                  // Print
  Serial.begin(9600);                   // Start aduino
  
}

void loop() {                           // Recive Data
  if (Serial.available() > 0) { 
    char incomingChar = Serial.read();  //Recive letters
    if (incomingChar == '*'){
        lcd.print("                ");  //Clear screen when recive '*'
    }
    Serial.print(incomingChar);
    lcd.print(incomingChar);            // Display the incoming character

  }
}