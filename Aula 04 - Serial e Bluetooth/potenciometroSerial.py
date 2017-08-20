import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.UART as UART
import serial
 
UART.setup("UART1")
ADC.setup()
 
ser = serial.Serial(port = "/dev/ttyO1", baudrate=9600)
value = ADC.read_raw("P9_40")

if ser.isOpen():
	print(value)
	ser.write(str(value) + "\n")
ser.close()

