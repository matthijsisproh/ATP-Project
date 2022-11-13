"""
Sensor objects:
DHT11
DFR0300
"""
import unittest
# from constants import *
from binding import c_DHT11
from typing import Generator, Union
import itertools
from statistics import mean
from decorators import logger, timer, cache
import doctest
from fractions import Fraction

class Sensor:
    def __init__(self):  #add class argument
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
        """mean(xs) is geen totale functie en kan errors geven. Beter checken we de lengte van de invoer, maar helaas heeft een
        generator geen lengte."""
        
        return mean(xs)
        # except StatisticsError:
        #     return None
    
    # @timer
    # @logger
    def measure_temperature(self, heat_power : int) -> Generator[int, None, None]:
        temperature = 0
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


class DHT11_Test(unittest.TestCase):
    def setUp(self):
        self._dht11_test = DHT11()
        self._c_dht11_test = None
    
    def test_safe_mean(self):
        if self._c_dht11_test != None:
            self.skipTest("DHT11 Sensor is available")

        for count in range(1, 100):
            generator = self._dht11_test.measure_temperature(count)
            result = self._dht11_test.safe_mean(itertools.islice(generator, count))
            self.assertAlmostEqual(result, self._dht11_test.safe_mean(itertools.islice(generator, 1))) #OK
            self.assertIsInstance(result, Union[None, float]) #OK
            self.assertIsInstance(result, float) #OK
            
    @unittest.expectedFailure
    def test_measure_temperature(self):
        if self._c_dht11_test != None:
            self.skipTest("DHT11 Sensor is available")

        result = self._dht11_test.measure_temperature(10)
        self.assertIsInstance(result, int) #OK - Expected failure: Instance should be Generator
        self.assertEqual(result, 18) #OK - Expected failure: function doesn't return int

        
    def test_update(self):
        for count in range(0, 100):
            result = self._dht11_test.update(count)
            if self._c_dht11_test == None:
                self.assertEqual(self._dht11_test._value, 1.0175 ** count * 18 ) #OK

            self.assertIsNone(result) #OK
            

    def test_return_value(self):
        for count in range(0, 100):
            self._dht11_test.update(count)
            result = self._dht11_test.return_value()
            self.assertIsInstance(result, float) #OK
            self.assertIsNotNone(result) #OK


unittest.main()
