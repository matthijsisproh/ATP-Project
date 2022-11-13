from unit_test import DHT11


class MySystem:
    def __init__(self):
        self._external_system = DHT11()

    def handle_message(self, message):
        try:
            self._external_system.measure_temperature(message)
            return True

        except:
            return False

            
def test_MySystem():
    system = MySystem()
    good_message = 10
    bad_message = 100
    assert system.handle_message(good_message)
    assert not system.handle_message(bad_message)
