import ctypes


class c_DHT11:
    def __init__(self):
        self.c_dht11 = ctypes.CDLL("/home/matthijsisproh/ATP-Project/bindings/clibrary.so") #On linux ubuntu
        self._value = 0

    def update(self):
        temperature = self.c_dht11.update()
        self._value = temperature

    def get_value(self):
        return self._value
