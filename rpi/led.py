import RPi.GPIO as GPIO
import time
import sdUtil


class LEDClass:
    Pins = []

    def __init__(self):
        self.setupLeds()

    def setupLeds(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        for led in sdUtil.LEDs:
            GPIO.setup(sdUtil.LEDs[led], GPIO.OUT)
            self.Pins.append(sdUtil.LEDs[led])

    def celebration(self, cycles: int):
        for i in range(cycles):
            for pin in self.Pins:
                ledOn(pin)
                time.sleep(0.1)
                ledOff(pin)


def ledOn(pin: int):
    GPIO.output(pin, GPIO.HIGH)

def ledOff(pin: int):
    GPIO.output(pin, GPIO.LOW)
