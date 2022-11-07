"""
Entity objects:
Temperature
Humidity
Soundvalue
"""
from constants import *
from sensor import Sensor


class Entity:
    def __init__(self, sensor : Sensor):
        self._sensor = sensor
        self._temperature = 0
        self._humidity = 0
        self._soundvalue = 0
    
    def get_value(self):
        pass

    def update(self):
        pass

"""
Temperature
"""
class Temperature(Entity):
    def __init__(self, sensor : Sensor):
        self._sensor = sensor
        self._temperature = 0

    def get_value(self):
        return self._temperature

    def update(self):
        self._temperature = self._sensor.return_value()

    def __repr__(self):
        rep = "Temperature: " + str(self.get_value())
        return rep


"""
Humidity
"""
class Humidity(Entity):
    def __init__(self, sensor : Sensor):
        self._sensor = sensor
        self._humidity = 0

    def get_value(self):
        return self._humidity

    def update(self):
        self._humidity = self._sensor.return_value()

    def __repr__(self):
        rep = "Humidity: " + str(self.get_value())
        return rep


"""
Soundvalue
"""
class Soundvalue(Entity):
    def __init__(self, sensor : Sensor):
        self._sensor = sensor
        self._soundvalue = 0

    def get_value(self):
        return self._soundvalue

    def update(self):
        self._soundvalue = self._sensor.return_value()

    def __repr__(self):
        rep = "Soundlevel: " + str(self.get_value())
        return rep