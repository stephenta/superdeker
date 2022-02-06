from led import LEDClass, ledOn, ledOff
import sdUtil
import time


def test_all_leds():
    for i in range(len(sdUtil.LEDs)):
        print(sdUtil.LEDs[i])
        ledOn(LED.Pins[i])
        time.sleep(2)
        ledOff(LED.Pins[i])


def main():
    global LED
    LED = LEDClass()

    test_all_leds()
    

if __name__ == '__main__':
    main()