"""
Sensor objects:
DHT11
DFR0300
"""

from constants import *
from binding import c_DHT11
from typing import Generator, Union
import itertools
from statistics import mean
from decorators import logger, timer

class Sensor:
    def __init__(self): 
        self._value = 1

    def update(self) -> None:
        pass

    def return_value(self) -> float:
        return round(self._value, 2)


"""
DHT11
"""

class DHT11(Sensor):
    def __init__(self, c_dht11: c_DHT11 = None):
        Sensor.__init__(self)
        self._c_dht11 = c_dht11

    def safe_mean(self, xs: Generator[float, None, None]) -> Union[None, float]:
        try:
            return mean(xs)
        except StatisticsError:
            return None
    
    @timer
    @logger
    def measure_temperature(self, heat_power : int) -> Generator[int, None, None]:
        temperature = 20
        alive = True
        
        while(alive):
            temperature = 1.0175 ** heat_power * 18
            yield temperature

    
    def update(self, heat_power) -> None:
        if(self._c_dht11 == None):
            temps_below = self.measure_temperature(heat_power)
            temperature = self.safe_mean(itertools.islice(temps_below, 100))

        else:
            self._c_dht11.update()
            temperature = self._c_dht11.get_value()

        self._value = temperature



"""
DFR0300
"""
class DFR0300(Sensor):
    def __init__(self):
        Sensor.__init__(self)

    @logger
    def update(self, fan_power) -> None:
        soundlevel = sound_factor ** fan_power * 20
        self._value = soundlevel

