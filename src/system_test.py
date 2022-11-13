from actuator import Heatpad, Coolingfan
from sensor import DHT11
import unittest

class System_test():
    def __init__(self):
        # Quality criteria of system
        self._min_desired_temperature = 19
        self._max_desired_temperature = 32
        
        # Actuators
        self._heatpad = Heatpad()
        self._coolingfan = Coolingfan()
        
        # Sensors
        self._dht11 = DHT11()

        # Entities
        self._heatpad_power = 0
        self._coolingfan_power = 0
        self._measured_temperature = 0


    def run(self):
        # Start all with 0
        heatpad_power = 0
        coolingfan_power = 0
        measured_temperature = 0
        
        for setpoint in range(self._min_desired_temperature, self._max_desired_temperature):
            print(setpoint)
            self._heatpad.update(setpoint)
            self._heatpad_power = self._heatpad.get_power()     

            self._coolingfan.update(setpoint, self._heatpad_power)
            self._coolingfan_power = self._coolingfan.get_power()

            self._dht11.update(self._heatpad_power)
            self._measured_temperature = self._dht11.return_value()

            if(self._measured_temperature > self._max_desired_temperature or self._measured_temperature < self._min_desired_temperature):
                return False


test = System_test()
if(test.run() == False):
    print("System is not working according to the quality criteria")
else:
    print("The system works correctly")








