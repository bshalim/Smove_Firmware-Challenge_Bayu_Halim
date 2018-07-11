# Smove Firmware Challenge
This repo contains 2 source codes: Arduino and Raspberry Pi

# Raspberry_Pi_I2C_Master
A pyhton source code (.py) that runs on Raspberry PI. It acts as a I2C master that communicates with Arduino and UART Terminal, relaying information regarding fuel level to the terminal and responding to its instructions
  
# Arduino_I2C_Slave
An Arduino source code (.ino) that runs on Arduino Uno. It acts as a I2C slave that receives instructions from the master (Raspberry      PI) and as a power supply to Raspberry Pi. Arduino is connected to two relays, which will turn active high or low depending on            Master's instructions, and a fuel sensor that updates the fuel level every second as requested by the Master.

## Bytes Used
I2C arbitrary bus address is 0x08
