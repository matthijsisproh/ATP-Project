import ctypes

clibrary = ctypes.CDLL("/home/matthijsisproh/ATP-Project/bindings/clibrary.so")
clibrary.display()