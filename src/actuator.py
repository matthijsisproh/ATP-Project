"""
Actuator:
Coolingfan
Heatpad
"""
from constants import *

class Actuator():
    def __init__(self):  #add class argument
        self._value = 0
        self._power = 0

    def get_power(self):
        return self._power

    def update(self) -> None:
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

    def update(self) -> None:
        self._power += 888


"""
Heatpad
"""
class Heatpad(Actuator):
    def __init__(self):  #add class argument
        self._value = 0
        self._power = 0     # an integer between 0 and 100
            
    def get_power(self):
        return self._power

    def simulate(temp):
        def update(self):
            if(self._power < 100):
                self._power += 1
        return update
    
    @simulate
    def update(self) -> None:
        self._power += 1


