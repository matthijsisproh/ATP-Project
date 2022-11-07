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
        self._unit_of_measure = ''

    def update(self, power = 0) -> None:
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
        self._unitOfMeasure = u'\xb0C'

    def simulate(tmp):
        def update(self, power):
            temperature = heat_factor ** power * 15
            self._value = temperature
        return update
            
    @simulate
    def update(self, power = 0) -> None:
        print(self._value)

    def _convertToValue(self) -> float:
        return round(self._value, 2)

    def return_value(self) -> float:
        return round(self._value, 2)

    def __repr__(self) -> str:
        rep = "Temperature: " + str(self._value)
        return rep

"""
DFR0300
"""
class DFR0300(Sensor):
    def __init__(self):
        Sensor.__init__(self)
        self._unitOfMeasure = u'\xb0C'

    def simulate(tmp):
            def update(self, power):
                temperature = sound_factor ** power * 20
                self._value = temperature
                print(self._value)
            return update

    @simulate
    def update(self, power = 0) -> None:
        self._value += 1

    def _convertToValue(self) -> float:
        return round(self._value, 2)

    def return_value(self) -> float:
        return self._value

    