import RPi.GPIO as GPIO
import i2c
import time
import os

# adjust for where your switch is connected
buttonPin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin, GPIO.IN)

led = i2c.I2C()
allLEDs = range(2,16)

while True:
  for i in allLEDs:
    led.setPWM(i, 4095)
  time.sleep(0.5)

  for i in allLEDs:
    led.setPWM(i, 0)
  time.sleep(0.5)

  # assuming the script to call is long enough that we can ignore bouncing
  if GPIO.input(buttonPin):
    os.system("python /home/pi/start.py")
