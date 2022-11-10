#include <iostream>

class DHT11(uint8_t pin, uint8_t type){
    _pin = pin;
    }

    public:
    float read_temperature(bool force){
        float f = NAN;

        if (read(force)){
            f = data[2];
            if(data[3] & 0x80){
                f = -1 - f;
            }
            f += (data[3] & 0x0f) * 0.1;
        }
        return f;
    }

    float read_humidity(bool force){
        float f = NAN;
        if(read(force)){
            f = data[0] + data[1] * 0.1;
        }
        return f;
    }

    bool read(bool force){
        uint32_t currenttime = millis();
        if(!force && ((currenttime - _lastreadtime) < MIN_INTERVAL)){
            return _lastresult;
        }
        _lastreadtime = currenttime;
    
        // Reset 40 bits of received data to zero.
        data[0] = data[1] = data[2] = data[3] = data[4] = 0;

        // Go into high impedence state to let pull-up raise data line level and
        // start the reading process.
        pinMode(_pin, INPUT_PULLUP);
        delay(1);

        pinMode(_pin, OUTPUT);
        digitalWrite(_pin, LOW);
        delay(20);  // data sheet says at least 18ms, 20ms just to be safe

        uint32_t cycles[80];
        {
            
            pinMode(_pin, INPUT_PULLUP);

            delayMicroseconds(pullTime);

            InterruptLock lock;
           
            if (expectPulse(LOW) == TIMEOUT) {
            DEBUG_PRINTLN(F("DHT timeout waiting for start signal low pulse."));
            _lastresult = false;
            return _lastresult;
            }
            if (expectPulse(HIGH) == TIMEOUT) {
            DEBUG_PRINTLN(F("DHT timeout waiting for start signal high pulse."));
            _lastresult = false;
            return _lastresult;
            }

            for (int i = 0; i < 80; i += 2) {
            cycles[i] = expectPulse(LOW);
            cycles[i + 1] = expectPulse(HIGH);
            }

        for (int i = 0; i < 40; ++i) {
            uint32_t lowCycles = cycles[2 * i];
            uint32_t highCycles = cycles[2 * i + 1];
            if ((lowCycles == TIMEOUT) || (highCycles == TIMEOUT)) {
            DEBUG_PRINTLN(F("DHT timeout waiting for pulse."));
            _lastresult = false;
            return _lastresult;
            }
            data[i / 8] <<= 1;
            // Now compare the low and high cycle times to see if the bit is a 0 or 1.
            if (highCycles > lowCycles) {
            // High cycles are greater than 50us low cycle count, must be a 1.
            data[i / 8] |= 1;
            }     
        }
        DEBUG_PRINTLN(F("Received from DHT:"));
        DEBUG_PRINT(data[0], HEX);
        DEBUG_PRINT(F(", "));
        DEBUG_PRINT(data[1], HEX);
        DEBUG_PRINT(F(", "));
        DEBUG_PRINT(data[2], HEX);
        DEBUG_PRINT(F(", "));
        DEBUG_PRINT(data[3], HEX);
        DEBUG_PRINT(F(", "));
        DEBUG_PRINT(data[4], HEX);
        DEBUG_PRINT(F(" =? "));
        DEBUG_PRINTLN((data[0] + data[1] + data[2] + data[3]) & 0xFF, HEX);

        // Check we read 40 bits and that the checksum matches.
        if (data[4] == ((data[0] + data[1] + data[2] + data[3]) & 0xFF)) {
            _lastresult = true;
            return _lastresult;
        } else {
            DEBUG_PRINTLN(F("DHT checksum failure!"));
            _lastresult = false;
            return _lastresult;
        }
    }

    uint32_t expect_pulse(bool level){
        #if (F_CPU > 16000000L) || (F_CPU == 0L)
        uint32_t count = 0;
        #else
        uint16_t count = 0; // To work fast enough on slower AVR boards
        #endif
        // On AVR platforms use direct GPIO port access as it's much faster and better
        // for catching pulses that are 10's of microseconds in length:
        #ifdef __AVR
        uint8_t portState = level ? _bit : 0;
        while ((*portInputRegister(_port) & _bit) == portState) {
            if (count++ >= _maxcycles) {
            return TIMEOUT; // Exceeded timeout, fail.
            }
        }
        // Otherwise fall back to using digitalRead (this seems to be necessary on
        // ESP8266 right now, perhaps bugs in direct port access functions?).
        #else
        while (digitalRead(_pin) == level) {
            if (count++ >= _maxcycles) {
            return TIMEOUT; // Exceeded timeout, fail.
            }
        }
        #endif

        return count;
    }

    private:
    uint8_t _pin, _type;
};

int main(){
    std::cout << "Hello world!";
}



DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  Serial.println(F("DHTxx test!"));

  dht.begin();
}

void loop() {
  // Wait a few seconds between measurements.
  delay(2000);

  // Reading temperature or humidity takes about 250 milliseconds!
  // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
  float h = dht.readHumidity();
  // Read temperature as Celsius (the default)
  float t = dht.readTemperature();
  
  // Check if any reads failed and exit early (to try again).
  if (isnan(h) || isnan(t)) {
    Serial.println(F("Failed to read from DHT sensor!"));
    return;
  }

  // Compute heat index in Celsius (isFahreheit = false)
  float hic = dht.computeHeatIndex(t, h, false);

  Serial.print(F("Humidity: "));
  Serial.print(h);
  Serial.print(F("%  Temperature: "));
  Serial.print(t);
  Serial.print("\n");
  
}