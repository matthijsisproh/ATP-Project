"""
Sensor objects:
DHT11
DFR0300
"""
import random
import unittest
from constants import *
import math

class Sensor:
    def __init__(self):  #add class argument
        self._value = 1
        

    def update(self) -> None:
        pass

    def read_value(self) -> float:
        return round(self._value, 2)

    def measure(self) -> str:
        return str(self._convert_to_value()) + self._unit_of_measure

    def _convert_to_value(self) -> float:
        return round(self._value, 2)

    def return_value(self) -> float:
        return round(self._value, 2)


"""
DHT11
"""
class DHT11(Sensor):
    def __init__(self):
        Sensor.__init__(self)

    def update(self, heat_power) -> None:
        # temperature = heat_factor ** heat_power * 15
        temperature = 30
        self._value = temperature

    def _convertToValue(self) -> float:
        return round(self._value, 2)

    def return_value(self) -> float:
        return round(self._value, 2)

"""
DFR0300
"""
class DFR0300(Sensor):
    def __init__(self):
        Sensor.__init__(self)

    def update(self, fan_power) -> None:
        soundlevel = sound_factor ** fan_power * 20
        self._value = soundlevel

    def _convertToValue(self) -> float:
        return round(self._value, 2)

    def return_value(self) -> float:
        return self._value

    