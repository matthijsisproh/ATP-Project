"""
Actuator:
Coolingfan
Heatpad
"""
from constants import *
import math

class Actuator():
    def __init__(self):  #add class argument
        self._value = 0
        self._power = 0

    def get_power(self):
        return self._power

    def update(self, power) -> None:
        pass

"""
Coolingfan
"""
class Coolingfan(Actuator):
    def __init__(self):  #add class argument
        self._value = 0
        self._power = 0

    def get_power(self):
        return self._power

    def update(self, temperature, heat_power) -> None:
        power = abs(math.log(temperature/heat_power)/ math.log(fan_factor)) 
        self._power = power
    
    def __repr__(self):
        rep = "Fan Power: " + str(self.get_power())
        return rep


"""
Heatpad
"""
class Heatpad(Actuator):
    def __init__(self):  #add class argument
        self._value = 0
        self._power = 0     # an integer between 0 and 100
            
    def get_power(self):
        return self._power

    def update(self, temperature) -> None:    
        power = math.log(temperature/temp_min) / math.log(heat_factor)
        self._power = power

    def __repr__(self):
        rep = "Heatpad Power: " + str(self.get_power())
        return rep


