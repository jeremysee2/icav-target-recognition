from typing import Tuple
import cv2
import numpy as np

import ICAV.GPSposition
import ICAV.altitude

class ImageRecognition():
    def __init__(self) -> None:
        self.altitude   = ICAV.altitude.Altitude()
        self.GPS        = ICAV.GPSposition.GPSPosition()
        self.image      = None
        self.targetGPS  = None

    def captureImage(self) -> None:
        pass

    def calculateTargetInImage(self) -> None:
        pass

    """
    Method to calculate the target GPS based on its position in the image.
    @returns: (lat,long) of the target
    """
    def calculateTargetGPS(self) -> Tuple[float, float]:
        pass