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

    def update_sensor(self) -> None:
        for sensor in self._control_sensors.values():
            if(self._is_simulation):
                for power in range(0, 100):
                    sensor.update(power)
                    
            else:
                sensor.update()

    def update_actuators(self) -> None:
        for actuator in self._control_actuators.values():
            actuator.update()

    def update_entities(self) -> None:
        for entity in self._control_entities.values():
            entity.update()

    
    def update(self) -> None:
        self.update_sensor()
        self.update_actuators()
        self.update_entities()





