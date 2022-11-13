from sensor import DHT11
import itertools
import unittest

class Integration_test:
    def __init__(self):
        self._external_module = DHT11()

    def test_DHT11(self) -> bool:
        try:
            temperature_generator = self._external_module.measure_temperature(1)
            temperature_float = self._external_module.safe_mean(itertools.islice(temperature_generator, 1))
            self._external_module.update(1)
            result = self._external_module.return_value()
            return True
        
        except Exception:
            return False

            
def test_integration():
    integration = Integration_test()
    unittest.TestCase.assertTrue(integration.test_DHT11(), "Integration failed")


test_integration()