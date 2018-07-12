import time
import serial #https://pythonhosted.org/pyserial/pyserial_api.html
import smbus  #https://github.com/bivab/smbus-cffi
import threading #https://docs.python.org/3/library/threading.html


#constants
fuel_level = 0

relay1_ON  = 0x11
relay2_ON  = 0x21
relay1_OFF = 0x10
relay2_OFF = 0x20
check_fuel = 0x30

#configure I2C connection
arduino_address = 0x08
bus = smbus.SMBus(0) #port I2C0


# configure the serial connections
ser = serial.Serial(
    port='/dev/tty-ACM0',
    baudrate=9600,
    bytesize=EIGHTBITS
)

ser.flushInput()
ser.flushOutput()


if ser.is_open()
    ser.write("RESET")
else
    ser.open()
    
    
#fuel checking    
def check_fuel():
    threading.Timer(1.0, check_fuel).start() #thread this task to achieve fuel reading every second
    bus.write_byte(arduino_address, check_fuel)
    time.sleep(1)
    fuel_level = bus.read_byte(arduino_address)
    fuel_level = int(fuel_level) *0.0049/ 0.01 #conversion from 10-bit Arduino ADC value (0.0049V/unit) to 0.01V/unit
    ser.write("last fuel sensor read value ")
    ser.write(str(fuel_level))


while ser.is_open():
    data = ser.readline() #read data transmitted by UART Terminal
    
    #perform task according to instructions sent by UART Terminal
    if str(data) == "AT+RLYON=1":
        ser.write("OK")
        bus.write_byte(arduino_address, relay1_ON)
    elif str(data) =="AT+RLYON=2":
        ser.write("OK")
        bus.write_byte(arduino_address, relay2_ON)    
    elif str(data) =="AT+RLYOFF=1":
        ser.write("OK")
        bus.write_byte(arduino_address, relay1_OFF)
    elif str(data) =="AT+RLYOFF=2":
        ser.write("OK")
        bus.write_byte(arduino_address, relay2_OFF)
    elif str(data) =="AT+SENS=?":
        bus.write_byte(arduino_address, check_fuel)
        fuel_level = bus.read_byte(arduino_address)
        fuel_level = int(fuel_level) *0.0049/ 0.01 #conversion from 10-bit Arduino ADC value (0.0049V/unit) to 0.01V/unit
        ser.write("OK")
        ser.write(str(fuel_level))

    #periodically check fuel
    check_fuel()
    
    
