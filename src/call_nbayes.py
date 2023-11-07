import os
import ctypes

def call_nayes(training_file, test_file, result_file):
    if os.name == "nt":
        lib = ctypes.CDLL(r"/Users/gssan/OneDrive/Área de Trabalho/Evolutionary-Computation-for-Feature-Selection/src/nbayes.dll")
    
    else:
        lib = ctypes.CDLL("/home/yksh/Desktop/Evolutionary-Computation-for-Feature-Selection/nbayes.so")
    
    
    lib.call_nbayes.argtypes = (ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p)
    lib.call_nbayes.restype = ctypes.c_int
    
    training_file = training_file.encode("utf-8")
    test_file = test_file.encode("utf-8")
    result_file = result_file.encode("utf-8")

    lib.call_nbayes(training_file, test_file, result_file)
    
    
    return 0

if __name__ == "__main__":
    call_nayes("./datasets/treino1.arff", "./datasets/teste1.arff", "./datasets/result.txt")