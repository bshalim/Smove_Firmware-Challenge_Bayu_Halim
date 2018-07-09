#include <Wire.h>

//pin initialization
int pi_power = 7;
int relay_1 = 3;
int relay_2 = 5;
int fuel_sensor = A0;

//temp variables
byte at_commands;
int fuel_level;

void setup() 
{
  //setting up I/O pins
  pinMode(pi_power, OUTPUT);
  pinMode(relay_1, OUTPUT);
  pinMode(relay_2, OUTPUT);
  pinMode(fuel_sensor, INPUT);
  digitalWrite(pi_power, HIGH);
  
  //initiate I2C transmission
  Wire.begin(8); //arbitrary address of I2C master
  Wire.onRequest(requestEvent);
  Wire.onReceive(receiveEvent);
}

void loop() 
{
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
 // start_time = millis();

}

//execute when data is requested
void requestEvent()
{
  Wire.write(fuel_level);
}

//execute when data is received
void receiveEvent(int numBytes)
{
  at_commands = Wire.read();
}

