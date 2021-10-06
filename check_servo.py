
PIN=14

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)

pwm = GPIO.PWM(PIN, 50)
pwm.start(0)

def SetAngle(angle):
	duty = angle/18+2
	GPIO.output(PIN, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(PIN, False)
	pwm.ChangeDutyCycle(0)
print("angle 0")
SetAngle(0)
sleep(0.5)

print("angle 45")
SetAngle(45)
sleep(0.5)

print("angle 90")
SetAngle(90)
sleep(0.5)

print("angle 180")
SetAngle(180)
sleep(0.5)

print("done")
GPIO.cleanup()
	
	

