import time
import serial #https://pythonhosted.org/pyserial/pyserial_api.html
import smbus  #https://github.com/bivab/smbus-cffi


#constants
relay1_ON  = 0x11
relay2_ON  = 0x21
relay1_OFF = 0x10
relay2_OFF = 0x20

#configure I2C connection
arduino_address = 0x55
bus = smbus.SMBus(0) #port I2C0


# configure the serial connections
ser = serial.Serial(
    port='/dev/tty-ACM0',
    baudrate=9600,
)

ser.flushInput()
ser.flushOutput()


try:
    ser.Open()

except Exception as e:
    print ("error opening serial port: " + str(e))
    exit()
    



while ser.is_open():
    data = ser.readline()
    temp_data
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
        bus.read_byte(arduino_address, temp_data)
        temp_data = float(temp_data) * 0.01
        ser.write("OK")
        ser.write(str(temp_data))
               
 





