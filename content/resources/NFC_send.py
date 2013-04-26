import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
#turn on pin 4 and set to 64KHz
GPIO.setup(4,GPIO.ALT0)
GPIO.setclock(4,64000)

def isBinary(binString):
	for char in binString:
		if ((char != '1') and (char != '0')):
			print(char + " is not valid")
			return False
	return True

while True:
	input = raw_input('enter binary string, e.g. 01110101 : ')
	if (isBinary(input)):
		count = 0
		for char in input:
			if (count ==0):
				GPIO.output(4,1)
				time.sleep(0.1)
			GPIO.output(4,int(char))
			time.sleep(0.1)
			count +=1
			if (count ==8):
				GPIO.output(4,1)
				time.sleep(0.1)
				GPIO.output(4,0)
				time.sleep(1)
				count = 0
		if (count >0):
			while (count <8):
				time.sleep(0.1)
				count +=1
			GPIO.output(4,1)
			time.sleep(0.1)
			GPIO.output(4,0)
			time.sleep(0.1)
	else:
		print("you may only enter 1s and 0s")
