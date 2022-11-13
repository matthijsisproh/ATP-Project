"""
Sensor objects:
DHT11
DFR0300
"""
import unittest
from constants import *
from binding import c_DHT11
from typing import Generator, Union
import itertools
from statistics import mean
from decorators import logger, timer
from sensor import DHT11

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
