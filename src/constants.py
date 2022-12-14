import math

"""Constants for physical simulation"""
temp_decay = 0.85       # Amount of temperature loss (in degrees celsius) when heater is off

temp_environment = 20   # Standard environment temperature. 

temp_conversion = 1.15  # 0.00V = 0.0 degrees celsius; steps of 0.05V per degree celsius above 0

"""Set Points: these indicate the desired values for the system"""
temp_setpoint = 15      # degrees celsius

"""Reaction difference: the amount of points of divergence allowed before the controller reacts"""
temp_reaction = 0.05


"""Heatpad"""
heatpad_max = 85        # Maximum heat of heatpad degree celsius

"""Desired temperatures degree celsius"""
temp_max = 30           # Maximum desired temperature degree celsius    
temp_min = 18           # Minimum desired temperature degree celsius


"""Formula factors"""
heat_factor = 1.0175
sound_factor = 1.015
fan_factor = 0.98964



