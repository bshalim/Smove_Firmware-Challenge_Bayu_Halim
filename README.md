This repo contains 2 files:
  1. A pyhton source code (.py) that runs on Raspberry PI. It acts as a I2C master that communicates with Arduino and UART Terminal
  2. An Arduino source code (.ino) that runs on Arduino Uno. It acts as a I2C slave that receives instructions from the master (Raspberry      PI) and as a power supply to Raspberry Pi. Arduino is connected to two relays, which will turn active high or low depending on            Master's instructions, and a fuel sensor that updates the fuel level every second as requested by the Master.
  
  I2C arbitrary bus address is 0x08
