class Effector:
    def __init__(self, heatfan_power=0, fan_power=0, temperature=20, humidity=0, soundlevel=20):
        self._heatfan_power = heatfan_power
        self._fan_power = fan_power
        self._temperature = temperature
        self._humidity = humidity
        self._soundlevel = soundlevel

    def update(self):
        if(self._heatfan_power < 100):
            self._heatfan_power += 1
        if(self._fan_power < 100):
            self._fan_power += 1
        
        if(self._temperature > 15 and self._temperature < 85):
            self._temperature += 1
        
        if(self._humidity < 100):
            self._humidity += 1

        if(self._soundlevel < 85):
            self._soundlevel += 1
        
    