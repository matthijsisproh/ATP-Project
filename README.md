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



### Coverage Report
![Coverage Report](\img\coverage report 2.png "")

### Reflection

