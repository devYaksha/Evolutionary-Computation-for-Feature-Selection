import ctypes

# Load the shared library
nbayes_dll = ctypes.CDLL('/home/yksh/Desktop/Evolutionary-Computation-for-Feature-Selection/nbayes.so')

# Define the argument and return types for the function
nbayes_dll.call_nbayes.argtypes = [ctypes.c_char, ctypes.c_char, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
nbayes_dll.call_nbayes.restype = ctypes.c_int  # It returns an int, not a float

mlnp = b'n'  # Use 'b' to create bytes-like objects for char
usf = b'n' 
training_dataset = b'./datasets/treino1.arff'
test_dataset = b'./datasets/teste1.arff'
result_file = b'./results.txt'

result = nbayes_dll.call_nbayes(mlnp, usf, training_dataset, test_dataset, result_file)

if result != 0:
    print("Python Error: execution of call_nbayes.")
