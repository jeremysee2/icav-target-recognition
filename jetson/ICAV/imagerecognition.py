from typing import Tuple
import cv2
import numpy as np

import ICAV.GPSposition
import ICAV.altitude

class ImageRecognition():
    def __init__(self) -> None:
        self.altitude   = ICAV.altitude.Altitude()
        self.GPS        = ICAV.GPSposition.GPSPosition()
        self.img        = None
        self.targetGPS  = None

        # Prepare OpenCV


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

    """
    Preprocessing function to increase brightness of original image:
    """
    def increaseBrightness(self, value=30) -> None:
        hsv = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)

        lim = 255 - value
        v[v > lim] = 255
        #v[v <= lim] += value

        final_hsv = cv2.merge((h, s, v))
        self.img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)

    """
    Debugging: set a dummy image for testing
    """
    def setImage(self, image) -> None:
        self.img = image


if __name__ == '__main__':
    from matplotlib import pyplot as plt
    imgrec = ImageRecognition()

    # Read in test image
    img_original = cv2.imread('IMG_3084.JPG')
    imgrec.setImage(img_original)

    # Test target recognition
    imgrec.calculateTargetInImage()

    # Test GPS calculation
    lat, long = imgrec.calculateTargetGPS()
    print(f'Target lat, long: ({lat}, {long})')