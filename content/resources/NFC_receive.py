
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
#setup listening pin
GPIO.setup(17,GPIO.IN)
simple_period = 0.1

#main loop
while True:
	#wait for first bit, should hear within 0.02 seconds to give us leeway
	while (not GPIO.input(17)):
		time.sleep(simple_period/5)
	message = ""
	time.sleep(simple_period/2)
	for i in range(8):
		high = 0
		time.sleep(simple_period/2)
		for j in range(5):
			high += GPIO.input(17)
			time.sleep(simple_period/10)
		message += str(int((high>=3)))
		
	time.sleep(simple_period)
	if (GPIO.input(17)):
		#if end bit is high
		print("Message received: " + message)
	else:
		print("Message has been corrupted")
	#ensure we do not read end byte again as start
	time.sleep(0.1)
