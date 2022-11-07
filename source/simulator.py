from entities import Entity, Temperature, Humidity, Soundvalue
from sensor import Sensor, DHT11, DFR0300
from actuator import Actuator, Coolingfan, Heatpad
from object_control import ObjectControl

from typing import Dict

class Simulator:
    def __init__(self):
        self._sensors = {
            'DHT11':DHT11(), 
            'DFR0300':DFR0300()
            }
        self._actuators = {
            'cooling': Coolingfan(),
            'heating': Heatpad()
            }
        self._entities = {
            'temperature': Temperature(self._sensors['DHT11']),
            'humidity': Humidity(self._sensors['DHT11']),
            'soundvalue': Soundvalue(self._sensors['DFR0300'])
            }
        

    def run(self):
        object_control = ObjectControl(self._sensors, self._actuators, self._entities, is_simulation=True)
        object_control.update()



