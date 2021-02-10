import RPi.GPIO as GPIO
import time, sys
from gpiozero import Button
pulse_pin = 22
RELAIS_1_GPIO = 23
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pulse_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT)
def countPulse1(channel):
	print("Water Flowing")

def pushChem1(channel):
	print("Water Flowing: Activating Chemical Pump")
	GPIO.output(RELAIS_1_GPIO, GPIO.HIGH)

GPIO.add_event_detect(pulse_pin, GPIO.RISING, callback=pushChem1)

try:
	while True:
		print("Water Not Flowing: Chemical Pump Inactive")
		GPIO.output(RELAIS_1_GPIO, GPIO.LOW)
		time.sleep(10)
except KeyboardInterrupt:
	print ("**Override Enabled: Program Exiting**")
	GPIO.cleanup()
	sys.exit()
