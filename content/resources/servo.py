#threading PWM
import threading
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
class PWMMotor(threading.Thread):
	def __init__(self,pin,duty=1):
		threading.Thread.__init__(self)
		self.pin = pin
		self.duty = duty
		GPIO.setup(pin,GPIO.OUT)
		
	def setDuty(self,duty):
		if duty > 2:
			self.duty = 2
		elif duty < 1:
			self.duty = 1
		else:
			self.duty = duty
		
	def run (self):
		while True:
			GPIO.output(self.pin,1)
			time.sleep((20-self.duty)/1000.0)
			GPIO.output(self.pin,0)
			time.sleep((self.duty)/1000.0)
			#print(self.duty)

if __name__ == "__main__":
	print("running PWM test")
	motor1 = PWMMotor(4,1.5)
	motor1.daemon = True
	motor1.start()
	#for i in xrange(1000):
	#	print i
	time.sleep(2)
	motor1.setDuty(1)
	time.sleep(2)
	motor1.setDuty(1.1)
	time.sleep(2)
	motor1.setDuty(1.2)
	time.sleep(2)
	motor1.setDuty(2)
	time.sleep(2)
	motor1.setDuty(1.7)
	time.sleep(2)
	motor1.setDuty(1.5)
	time.sleep(30)
	GPIO.output(4,False)
