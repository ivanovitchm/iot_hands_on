import Adafruit_BBIO.GPIO as GPIO
import time

GPIO.setup("P9_27", GPIO.IN)

while True:
	if GPIO.input("P9_27"):
		print("HIGH")
	else:
		print("LOW")
	time.sleep(1)


