import os
import ctypes


training_file = "./datasets/treino1.arff"
test_file = "./datasets/teste1.arff"
result_file = "./datasets/result.txt"

lib = ctypes.CDLL("C://Users/gssan/OneDrive/Área de Trabalho/Evolutionary-Computation-for-Feature-Selection/nbayes.dll")
lib.call_nbayes.argtypes = (ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p)
lib.call_nbayes.restype = ctypes.c_int


#__declspec(dllexport) int call_nbayes(string training_dataset, string test_dataset, string result_file)
lib.call_nbayes(training_file, test_file, result_file)