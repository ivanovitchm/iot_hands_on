import Adafruit_BBIO.UART as UART
import serial
 
UART.setup("UART1")
 
ser = serial.Serial(port = "/dev/ttyO1", baudrate=9600)
if ser.isOpen():
	print("Serial is open!")
	ser.write("Hello World!")
ser.close()

