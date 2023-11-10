import os
import ctypes
import numpy as np

def call_nbayes(mlnp:str, usf:str, training_dataset:str, test_dataset:str, result_file:str):
    """Call nbayes function from nbayes.so, read docs/GMNB_2009_Silla.pdf for more information.
    
    Args:
        - mlnp (char 'y' or 'n'): Mandatory Leaf Node Prediction
        - usf (char 'y' or 'n'): Usefulness
        - training_dataset (str): path
        - test_dataset (str): path
        - result_file (str): path
    """

    if not os.path.exists('./src/nbayes.so'):
        print("Error: nbayes.so not found.")
        return
    
    if os.name == 'nt':
        print("Error: nbayes.so is not compatible with Windows yet.")
        return

    nbayes_dll = ctypes.CDLL('./src/nbayes.so')

    nbayes_dll.call_nbayes.argtypes = [ctypes.c_char, ctypes.c_char, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
    nbayes_dll.call_nbayes.restype = ctypes.c_float

    # Use 'b' to create bytes-like objects 
    mlnp = bytes(mlnp, 'utf-8')
    usf = bytes(usf, 'utf-8')
    training_dataset = bytes(training_dataset, 'utf-8')
    test_dataset = bytes(test_dataset, 'utf-8')
    result_file = bytes(result_file, 'utf-8')

    result = float(nbayes_dll.call_nbayes(mlnp, usf, training_dataset, test_dataset, result_file))

    #print("Result: ", result) # Long double -> float
    
    return result


call_nbayes('y', 'y', './datasets/treino1.arff', './datasets/teste0.arff', './datasets/results.txt')