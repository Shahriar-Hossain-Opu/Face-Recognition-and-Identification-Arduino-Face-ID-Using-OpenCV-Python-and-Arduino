// IF you are unable to upload the file to Arduino then uncomment the "Adafruit_SSD1306.h"
// and "SimpleDHT.h" 
//#include <Adafruit_SSD1306.h>
//#include <SimpleDHT.h>
#include <LiquidCrystal.h>

#define led 6
int data, flag = 2;

void setup()
{
  pinMode(led, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
  digitalWrite(led, LOW);
  digitalWrite(LED_BUILTIN, LOW);
 
}

void loop()
{
  while( Serial.available() )
  {
    data = Serial.read();

    if (data == '1')
    {
      flag = 1;
    }
    else if(data == '0')
    {
      flag = 0;
    }
  }
  if(flag == 1)
    {
  
      digitalWrite(led, HIGH);
      
      delay(2000);
      
      digitalWrite(LED_BUILTIN, HIGH);
    }
     else if (flag == 0)
    {
      
      digitalWrite(led, LOW);
      digitalWrite(LED_BUILTIN, LOW);
    }
}
