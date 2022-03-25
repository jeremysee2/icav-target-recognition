import ICAV.UAV as drone
import time

sleepTime = 1.0

if __name__ == '__main__':
    # Setup UAV
    uav = drone.UAV()
    targetLatitude, targetLongitude = 0.0, 0.0

    # Wait for sensors to be initialised
    while not uav.sensorsReady():
        time.sleep(0.2)

    # Infinite loop to run at a set interval
    while True:
        # Query data from all sensors
        uav.imgrec.altitude.queryAltitude()
        uav.imgrec.GPS.queryPosition()
        uav.imgrec.captureImage()

        # Calculate position of target in image
        targetLatitude, targetLongitude = uav.imgrec.calculateTargetGPS()

        # Send data out via LoRa
        uav.sendTargetGPSToLora(targetLatitude, targetLongitude)

        # Wait for next interval
        time.sleep(sleepTime)
    pass