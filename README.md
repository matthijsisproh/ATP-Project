# ATP-Project

This project contains an implementation and is built with the Function Reactive Programming  and Aspect Oriented programming principles. 

In this project is a simulation of the modules:
- DHT11: Humidity and Temperature Sensor
- DFR0300: DF Robot Sound level Sensor
- Heatpad: Heating element
- Coolingfan: Fan for cooling

This project also includes a binding between C++ and Python to control the DHT11 Sensor.(No simulation)

Although the project created has been tested by Unittests(Only DHT11 module), Integration tests and a system test.

## Usage
To run the simulation type in terminal "python3 src/main.py"

## Test report
To run test ...

### Unit Test
DHT11 module all functions tested passed.

#### Functions:
- safe_mean : This function returns an Union[None, float] type, this function returns a mean value of measure_temperature
- measure_temperature : This function returns a Generator[int, None, None] type, this function returns the measured temperature
- update : This function returns a None type, this function updates the temperature by calling measure_temperature
- return_value : This function returns a float, this function is a get function of DHT11 Module.

### Integration Test
- 


### System Test



### Coverage
The results of code coverage allow us to measure how much of the code is actually used.

#### Coverage & Branch Coverage Report
![Coverage Report](https://imgur.com/uRU4ZsW.png "")
![Branch Report](https://i.imgur.com/lZISxiI.png "")

In the coverage and branch coverage report we can find out what code is covered and what not. The reason why actuator.py, entities.py and sensor.py are not fully covered is because those files exists out of superclass Actuator, Entity and Sensor. Those superclasses is not often used because you don't need to call these classes external. The next thing is why binding.py has a coverage of 50% is because it is not used when simulation is on.


### Reflection

