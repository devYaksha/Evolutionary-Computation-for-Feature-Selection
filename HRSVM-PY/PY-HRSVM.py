import ctypes
import os
from subprocess import call
call(["ls", "-l"])

"""
Use of ctypes: 
#gcc -fPIC -shared -o helloworld.so hello.c
#g++ -fPIC -shared -o helloworld.so hello.cpp
lib = ctypes.CDLL("HRSVM-PY/helloworld.so")

"""

def svmTrain(classifierKernel, trainDataBase, outputFolder):
    os.system(f'./HRSVM-PY/HRSVM/svm-train -k {classifierKernel} -a 1 "{trainDataBase}" "{outputFolder}"')





svmTrain("binary", "/home/yksh/Desktop/GAs-for-Hierarchical-Classification/tests/train.dat", "/home/yksh/Desktop/GAs-for-Hierarchical-Classification/tests/output")