"""
Altitude sensor module, BME280.
Interfaces with BME280 using the Sparkfun library over I2C.
"""

from __future__ import print_function
import qwiic_bme280
import time
import sys

#The name of this device
_DEFAULT_NAME = "Qwiic BME280"

_AVAILABLE_I2C_ADDRESS = [0x77, 0x76]

#Default Setting Values
_settings = {"runMode" : 3,         \
            "tStandby" : 0,         \
            "filter"   : 0,         \
            "tempOverSample"  : 1,  \
            "pressOverSample" : 1,  \
            "humidOverSample" : 1,  \
            "tempCorrection"  : 0.0}

#define our valid chip IDs
_validChipIDs = [0x58, 0x60]


class Altitude():
    def __init__(self) -> None:
        # Initialise sensor
        self.mySensor = qwiic_bme280.QwiicBme280()
        if self.mySensor.connected == False:
            raise ConnectionError
        self.mySensor.begin()

        # Memory to save last known altitude
        self.altitude = 0.0

    def queryAltitude(self) -> float:
        return self.altitude

    def getAltitude(self) -> None:
        self.altitude = self.mySensor.altitude_feet

if __name__ == '__main__':
    try:
        bme280 = Altitude()
        print(f'Current Altitude: {bme280.getAltitude()}')
    except ConnectionError as exErr:
        print("The Qwiic BME280 device isn't connected to the system. Please check your connection")
    else:
        print("Example ended successfully")