
PIN=21
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN)

print("push 3 times")
click_cnt = 0
while click_cnt < 3:
	inputValue = GPIO.input(PIN)
	if inputValue == False:
		click_cnt = click_cnt + 1
		print(click_cnt)
	sleep(0.3)
	
print("done")
GPIO.cleanup()
