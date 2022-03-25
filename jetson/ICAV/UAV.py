import serial

import ICAV.altitude
import ICAV.imagerecognition

class UAV():
    def __init__(self) -> None:
        self.imgrec     = ICAV.imagerecognition.ImageRecognition()

    """
    Send data out via UART to ESP32 Gateway, to be sent back to the Ground Station.
    """
    def sendTargetGPSToLora(self, latitude, longitude) -> None:
        pass

    """
    Checks that all sensors are connected and ready to go.
    In particular, GPS needs a fix to function properly.
    """
    def sensorsReady() -> bool:
        return True