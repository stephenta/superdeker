from game.arduinoConnection import ArduinoClass, waitForSensor
from game.led import LEDClass, ledOn, ledOff

from random import randint
from datetime import datetime

ARDUINO = None
LED = None

POINT_TARGET = 20


def game():
    print("Game start")
    state = 0

    while state < len(LED.Pins):
        print("State: " + str(state))
        ledOn(LED.Pins[state])
        waitForSensor(ARDUINO.Sensors[state])
        ledOff(LED.Pins[state])
        state += 1

    print("Game over")
    LED.celebration(5)
    return

def pickSensorIndex():
    return randint(0, 9)


def waitForPoint(index, arduino, led):
    # turn on led, wait for sensor to trigger, turn off led
    ledOn(led.Pins[index])
    waitForSensor(arduino.Sensors[index])
    ledOff(led.Pins[index])


def timeAttack():
    """
        Give user 1 min to get as many points as they can.
    """
    pass


def pointRace(arduino, led):
    """
        Records time that it takes for a user to get 20 points.
    """
    userPoints = 0

    # first sensor - not in loop because need to set start time once
    # it is taken
    currentSensor = pickSensorIndex()
    waitForPoint(currentSensor, arduino, led)
    startTime = datetime.now()
    userPoints += 1
    lastSensor = currentSensor
    
    while userPoints < POINT_TARGET:
        # pick a sensor
        while currentSensor == lastSensor:
            currentSensor = pickSensorIndex()
        waitForPoint(currentSensor, arduino, led)
        userPoints += 1
        lastSensor = currentSensor

    userTime = datetime.now() - startTime
    print(userTime)

    led.celebration(5)

    return userTime



def insaneMode():
    """
        How many points a user can get when each light only
        lasts 2 secs.
    """
    pass


def play(arduino, led):
    return pointRace(arduino, led)
    

if __name__ == '__main__':
    play()
