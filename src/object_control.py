from entities import Entity
from sensor import Sensor
from actuator import Actuator

from typing import Dict

"""
ObjectControl
"""
class ObjectControl:
    def __init__(self, sensors: Dict[(str, Sensor)], actuators: Dict[(str, Actuator)], entities: Dict[(str, Entity)], is_simulation = False):
        self._control_sensors = sensors
        self._control_actuators = actuators
        self._control_entities = entities
        self._is_simulation = is_simulation
        self._temperature = 19

    def simulate(self, heatpower, fanpower):
        self._heatpower = heatpower
        self._fanpower = fanpower

    def update_sensor(self) -> None:
        self._control_sensors['DHT11'].update(self._heatpower)
        self._fanpower = self._control_actuators['cooling'].get_power()
        self._control_sensors['DFR0300'].update(self._fanpower)

    def update_actuators(self) -> None:
        self._control_actuators['heating'].update(self._temperature)
        self._heatpower = self._control_actuators['heating'].get_power()
        self._control_actuators['cooling'].update(self._temperature, self._heatpower)
        

    def update_entities(self) -> None: 
        for entity in self._control_entities.values():
            entity.update()

        self._temperature = self._control_entities['temperature'].get_value()


    def update(self) -> None:
        self.update_sensor()
        self.update_entities()
        self.update_actuators()





