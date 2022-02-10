import RPi.GPIO as GPIO
import time
import game.sdUtil as sdUtil


class LEDClass:
    Pins = []

    def __init__(self):
        self.setupLeds()

    def setupLeds(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        for pin in sdUtil.LEDs:
            GPIO.setup(pin, GPIO.OUT)
            self.Pins.append(pin)

    def celebration(self, cycles):
        for i in range(cycles):
            for pin in self.Pins:
                ledOn(pin)
                time.sleep(0.1)
                ledOff(pin)

    def clearLeds(self):
        for pin in self.Pins:
            ledOff(pin)


def ledOn(pin):
    GPIO.output(pin, GPIO.HIGH)

def ledOff(pin):
    GPIO.output(pin, GPIO.LOW)
