from entities import Entity, Temperature, Humidity, Soundvalue
from sensor import Sensor, DHT11, DFR0300
from actuator import Actuator, Coolingfan, Heatpad
from object_control import ObjectControl
from constants import *
from effector import Effector
from binding import c_DHT11

import time
from typing import Dict

class Simulator:
    def __init__(self):
        # self.c_dht11 = c_DHT11()
        self._sensors = {
            'DHT11':DHT11(), #self.c_dht11
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

        self._heatpower = 0
        self._fanpower = 0

    def print_state(self) -> None:
        for entity in self._entities.values():
            print(repr(entity))

        for actuator in self._actuators.values():
            print(repr(actuator))

    
    def run(self):
        timestamp = 0
        object_control = ObjectControl(self._sensors, self._actuators, self._entities, is_simulation=True)
        while(timestamp < 10):
            timestamp += 1
            self._heatpower += 1
            self._fanpower += 1
            # time.sleep(1)
            print(timestamp, '----------------------------------------')
            object_control.simulate(self._heatpower, self._fanpower)
            object_control.update()
            
            self.print_state()
        # object_control.print_cache()

    




