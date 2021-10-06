
import RPi.GPIO as GPIO
import cv2 as cv

LED_PIN = 23
SENS_PIN = 24

class Sens:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.IN)
    def read(self):
        return GPIO.input(self.pin)

class Led:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
    def turn(self, value):
        GPIO.output(self.pin, value)
        
led = Led(LED_PIN)
sens = Sens(SENS_PIN)
while True:
	led.turn(sens.read())
