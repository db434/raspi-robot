import RPi.GPIO as GPIO
import time

ledPin=9
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin,GPIO.OUT)
coilPin = 17
GPIO.setup(coilPin,GPIO.IN)
while True:
	GPIO.output(ledPin,GPIO.input(coilPin))
	time.sleep(0.1)
