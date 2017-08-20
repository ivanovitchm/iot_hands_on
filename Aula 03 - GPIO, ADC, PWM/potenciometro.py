import Adafruit_BBIO.ADC as ADC
import time

ADC.setup()

while True:
	valor = ADC.read_raw("P9_40")
	print(valor)
	time.sleep(1)
