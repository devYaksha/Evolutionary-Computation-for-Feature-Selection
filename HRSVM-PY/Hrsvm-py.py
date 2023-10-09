import ctypes

"""
Use of ctypes: 
#gcc -fPIC -shared -o helloworld.so hello.c
#g++ -fPIC -shared -o helloworld.so hello.cpp


"""

lib = ctypes.CDLL("HRSVM-PY/helloworld.so")

print(lib.sum(2,4))



