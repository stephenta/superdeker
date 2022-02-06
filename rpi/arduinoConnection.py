import time
import sdUtil

from pyfirmata import Arduino, util, INPUT


class ArduinoClass:
    Board = None
    Sensors = []

    def __init__(self):
        self.setupConnection()
        self.setupSensors()

    def setupConnection(self):
        # sets up connection with Arduino
        self.Board = Arduino(sdUtil.ArduinoPort)

        # Start iterator to receive input data
        it = util.Iterator(self.Board)
        it.start()

    def setupSensors(self):
        for sensor in sdUtil.ArduinoSensors:
            sen = self.Board.digital[sensor]
            sen.mode = INPUT
            self.Sensors.append(sen)


def waitForSensor(sensor):
    while True:
        sensorVal = sensor.read()
        if sensorVal:
            break

    return
