from arduinoConnection import ArduinoClass, waitForSensor
from led import LEDClass, ledOn, ledOff


ARDUINO = None
LED = None


def game():
    print("Game start")
    state = 0

    while state < 4:
        print("State: " + str(state))
        ledOn(LED.Pins[state])
        waitForSensor(ARDUINO.Sensors[state])
        ledOff(LED.Pins[state])
        state += 1

    print("Game over")
    LED.celebration(5)
    return


def main():
    global ARDUINO, LED
    ARDUINO = ArduinoClass()
    LED = LEDClass()

    game()
    

if __name__ == '__main__':
    main()
