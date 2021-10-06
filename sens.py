import RPi.GPIO as GPIO
import cv2 as cv
import numpy as np

SENS_PIN = 24
LED_PIN = 23

model = 'frozen_inference_graph.pb'
config = 'mobilenet_config.pbtxt'

freq = 25

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



class Camera:
    def __init__(self):
        self.cam = cv.VideoCapture(0)
        self.net = cv.dnn.readNetFromTensorflow(model, config)
        self.first_frame = None
        self.prev_frame = None
        self.count = 0
    def __del__(self):
        self.cam.release()
        cv.destroyAllWindows()

    def clear(self):
        black_screen = np.zeros([200, 200, 1], dtype=np.uint8)
        cv.imshow('stream', black_screen)

    def onUpdate(self):
        self.count += 1
        ret, frame = self.cam.read()
        if frame is None:
            return

        frame = cv.resize(frame, (200, 200))
        rows = frame.shape[0]
        cols = frame.shape[1]

        self.net.setInput(cv.dnn.blobFromImage(frame, size=(100, 100), swapRB=True, crop=False))
        netOut = self.net.forward()

        for detection in netOut[0, 0, :, :]:
            score = float(detection[2])
            if score > 0.5:
                idx = int(detection[1])

                #rect
                left = detection[3] * cols
                top = detection[4] * cols
                right = detection[5] * cols
                bottom = detection[6] * cols

                if idx == 1: #human
                    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
                    gray = cv.GaussianBlur(gray, (21, 21), 0)

                    if self.first_frame is None or self.count > freq and self.count % freq == 1:
                        self.prev_frame = frame
                        self.first_frame = gray

                    frame_delta = cv.absdiff(self.first_frame, gray)
                    thresh = cv.threshold(frame_delta, 70, 255, cv.THRESH_BINARY)[1]
                    thresh = cv.dilate(thresh, None, iterations=2)
                    contours, _ = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

                    for c in contours:
                        x, y, w, h = cv.boundingRect(c)
                        if left <= x <= right and top <= y <= bottom:
                            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 250), 2)
                cv.rectangle(frame, (int(left), int(top)), (int(right), int(bottom)), (23, 230, 210), thickness=2)
                y = int(top) - 15 if int(top) - 15 > 15 else int(top) + 15
                cv.putText(frame, str(idx), (int(left), y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (100, 100, 100), 2)
        cv.imshow('stream', frame)




if __name__ == "__main__":
    led = Led(LED_PIN)
    sens = Sens(SENS_PIN)
    cam = Camera()
    while True:

        value = sens.read()
        led.turn(value)
        if value:
            cam.onUpdate()
        else:
            cam.clear()

        k = cv.waitKey(30) & 0xff
        if k == 27:
            break
