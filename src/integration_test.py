from unit_test import DHT11


class MySystem:
    def __init__(self):
        self._external_system = DHT11()

    def test_DHT11(self):
        try:
            for heat_power in range(0, 100):
                temperature_int = self._external_system.measure_temperature(heat_power)
                temperature_float = self._external_system.safe_mean(temperature_int)
                self._external_system.update()
                result = self._external_system.return_value()
            print(temperature_int)
            print(temperature_float)
            print(result)
            return True

        except Exception:
            return False

            
def test_MySystem():
    system = MySystem()

    assert system.test_DHT11()
    assert not system.test_DHT11()

