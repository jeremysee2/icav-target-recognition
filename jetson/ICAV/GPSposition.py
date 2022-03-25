from ublox_gps import UbloxGps
import serial

class GPSPosition():
    def __init__(self) -> None:
        self.port = serial.Serial('/dev/serial0', baudrate=38400, timeout=1)
        self.gps = UbloxGps(self.port)
        self.coords = 0

    def __del__(self) -> None:
        self.port.close()
        pass

    def queryPosition(self) -> None:
        self.coords = self.gps.geo_coords()

    def getLatitude(self) -> float:
        return self.coords.lat

    def getLongitude(self) -> float:
        return self.coords.long
