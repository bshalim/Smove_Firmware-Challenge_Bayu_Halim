#include <Wire.h> //arduino wire library https://www.arduino.cc/en/reference/wire

//pin initialization
int pi_power = 7;
int relay_1 = 3;
int relay_2 = 5;
int fuel_sensor = A0;

//constants
long pi_reset_timer = 10000;

//temp variables
byte at_commands;
int fuel_level;
long start_timer;

void setup() 
{
  //setting up I/O pins
  pinMode(pi_power, OUTPUT);
  pinMode(relay_1, OUTPUT);
  pinMode(relay_2, OUTPUT);
  pinMode(fuel_sensor, INPUT);

  //Supply power to Raspberry Pi when Arduino boots
  digitalWrite(pi_power, HIGH);
  
  //initiate I2C transmission
  Wire.begin(0x08); //arbitrary address of Pi I2C
  Wire.onRequest(requestEvent);
  Wire.onReceive(receiveEvent);
}

void loop() 
{
  delay(100);
}

//execute when data is requested
void requestEvent()
{
  Wire.write(fuel_level);
}

//execute when data is received
void receiveEvent(int numBytes)
{
  if(Wire.available())
  {
    at_commands = Wire.read();
    switch(at_commands)
    {
      case 0x11:
        digitalWrite(relay_1, HIGH);
        break;

      case 0x21:
        digitalWrite(relay_2, HIGH);
        break;

      case 0x10:
        digitalWrite(relay_1, LOW);
        break;

      case 0x20:
        digitalWrite(relay_2, LOW);
        break;

      case 0x30:
        fuel_level = analogRead(fuel_sensor);
        break;
    }
  }

  //start timer when there is no data in the I2C Bus
  if(Wire.available() < 1)
  {
    start_timer = millis();   
  }

  //countdown timer, if there is no data in the I2C Bus for 10 seconds, reset Raspberry Pi
  while(Wire.available() < 1)
  {
    if(millis()-start_timer > pi_reset_timer)
    {
      reset_Pi();
      break;
    }
  }  
}

//function to reset power to Raspberry Pi
void reset_Pi()
{
  digitalWrite(pi_power, LOW);
  delay(1000);
  digitalWrite(pi_power, HIGH);
}
