import Adafruit_BBIO.PWM as PWM
import time

PWM.start("P8_19", 10)
PWM.set_duty_cycle("P8_19", 50.0)
PWM.set_frequency("P8_19", 2000)
time.sleep(2)
PWM.stop("P8_19")
PWM.cleanup()


