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
To run the simulation type in terminal:
```
python3 src/main.py
```

## Test report
To run test ...

### Unit Test
The unit_test.py file provides individual tests of the DHT11 module functions.
All functions tested passed.

To run the integration test in terminal:
```
python3 unit_test.py -v
```

#### Functions:
- safe_mean : This function returns an Union[None, float] type, this function returns a mean value of measure_temperature
- measure_temperature : This function returns a Generator[int, None, None] type, this function returns the measured temperature
- update : This function returns a None type, this function updates the temperature by calling measure_temperature
- return_value : This function returns a float, this function is a get function of DHT11 Module.


### Integration Test
For the integration test we used the so called "Big Bang Test" method. In big bang integration testing, all the different modules are integrated simultaneously.
All modules of DHT11 are integrated simultaneously to test the system as a whole. The modules are not tested individually. Instead, they are tested together once the entire system is complete.

To run the integration test in terminal:
```
python3 integration_test.py -v
```


### System Test
For the system test we want the system to return a measured temperature between 18 and 32 degrees celsius. For this we run heatpad and coolingfan.
After all this finished we want to see what is the measured temperature based on heatpad power and coolingfan power.

To run the system test in terminal:
```
python3 system_test.py -v
```

Output:
The system works.

The measured temperature based on heatpad and coolingfan power is between the quality criteria of 18 and 32 degrees celsius.



### Coverage
The results of code coverage allow us to measure how much of the code is actually used.

#### Coverage & Branch Coverage Report
![Coverage Report](https://imgur.com/uRU4ZsW.png "")
![Branch Report](https://i.imgur.com/lZISxiI.png "")

In the coverage and branch coverage report we can find out what code is covered and what not. The reason why actuator.py, entities.py and sensor.py are not fully covered is because those files exists out of superclass Actuator, Entity and Sensor. Those superclasses is not often used because you don't need to call these classes external. The next thing is why binding.py has a coverage of 50% is because it is not used when simulation is on.


### Reflection
For this project I am pity to say that it failed to connect the DHT11 module sensor to the arduino UNO and run it simultanously on the simulation. I am glad to say that the simulation works and all tests passed. I hope to finish this project with my new knowledge of functional reactive programming and aspect oriented programming. The binding of C++ and Python only works on my Linux VM, because I got many errors of saying that it is not a Win32 application.

I hope you enjoyed my project and feel free to give feedback.

