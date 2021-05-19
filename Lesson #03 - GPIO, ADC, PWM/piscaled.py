import Adafruit_BBIO.GPIO as GPIO
import time

GPIO.setup("P9_14", GPIO.OUT)
GPIO.output("P9_14", GPIO.HIGH)
time.sleep(4)
GPIO.output("P9_14", GPIO.LOW)
