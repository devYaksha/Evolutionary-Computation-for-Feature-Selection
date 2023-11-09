import math

def in_array(value:float, vector:list):
    """Verifica se o 'value' esta no 'vector'"""
    for i in range(len(vector)):
        if value == vector[i]:
            return i
    return -1


def distinct(categorical:list):
    """Recebe uma lista de valores categóricos e retorna uma lista de valores distintos"""
    vector_distinct = [categorical[0]]
    for i in range(1, len(categorical)):
        if in_array(categorical[i], vector_distinct) == -1:
            vector_distinct.append(categorical[i])

    return vector_distinct

def frequence_double(dist_class, vector_categorical):
    """Calcula a frequência de ocorrência de elementos do vetor categórico em relação a uma distribuição de classes."""
    frequence = [0 for i in range(len(dist_class))]
    for k in range(len(vector_categorical)):
        position = in_array(vector_categorical[k], dist_class)
        frequence[position] += 1
    
    return frequence

def explode(input_str, delimiter):
    """Recebe uma input_string e a 'quebra' e retorna em um vetor de pequenas sub-strings baseado no caractere delimitador"""
    out = []
    start = 0
    found = input_str.find(delimiter)

    while found != -1:
        sub_str = input_str[start:found]
        out.append(sub_str)
        start = found + 1
        found = input_str.find(delimiter, start)

    # Adiciona a ultima sub-string
    out.append(input_str[start:])

    return out

def in_array_string(v_class, vectorA):
    """Verifica se v_class está contida no vectorA, retornando sua posição."""
    for i in range(len(vectorA)):
        if v_class == vectorA[i]:
            return i
    
    return -1

def get_column(matrix, k):
    vector = []
    for j in range(len(matrix)):
        vector.append(matrix[j][k])
    return vector


#----------------------------------------------------------------------------------------------------------------------------------------------------------------


def sum_vc(vector: list):
    """Return the sum of a list.

    Returns:
        double: the sum of the list.
    """    
    return sum(vector)

def mean(vector: list):
    """

    Returns:
        double: the mean of the list.
    """    
    return sum_vc(vector)/len(vector)

def sqsum(vector:list):
    """

    Returns:
        double: Return the sum of the list squared.
    """    
    s = 0
    for i in range(len(vector)):
        s += pow(vector[i], 2)
    return s

def stdev(vector:list):
    """ 

    Returns:
        double: Return the standard deviation of a list.
    """    

    return math.sqrt(sqsum(vector))

def operatorMinus(vector: list, numSubtraction:float):
    """
    Returns:
        list: a vector with the elements subtracted by 'numSubtraction'.
    """    

    vectorCopy = vector[:]
    for i in range(len(vector)):
        vectorCopy[i] = vector[i] - numSubtraction
    return vectorCopy

def operatorMultiplication(vector:list, numMultiplication:float):
    """
    Returns:
        list: Return a list with the elements multiplied by 'numMultiplication'.
    """    

    vectorCopy = vector[:]
    for i in range(len(vector)):
        vectorCopy[i] = vector[i] * numMultiplication[i]
    return vectorCopy



def binaryVector(k:float, vector:list):  
    """

    Returns:
        list: Return a binary list, where the elements are 1 if the element of the vector is equal to 'k', and 0 otherwise.
    """    

    binary_vector = [0 for i in range(len(vector))]
    for i in range(len(vector)):
        if (vector[i] == k):
            binary_vector[i] = 1
    return binary_vector

def prob_a_and_b(vectorA:list, vectorB:list):
    """
    Args:
        vectorA (list): Binary list.
        vectorB (list): Binary list.

    Returns:
        float: Return the probability of the intersection between two vectors.
    """    

    sum_A_B = 0
    for i in range(len(vectorA)):
        if vectorA[i] == 1 and vectorB[i] == 1:
            sum_A_B += 1
    return sum_A_B / len(vectorA)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------


def class_level(possible_class):
    """percorre o vetor de classes possiveis e retorna um vetor de mesmo tamanho com o nivel da classe"""
    level_vector = []
    for i in range(len(possible_class)):
        aux_str = explode(possible_class[i], '.')
        level_vector.append(len(aux_str))
    return level_vector

def classes_per_level(max_level, possible_class_level):
    """percorre o vetor de classes possiveis e retorna um vetor com o total de classes por nivel da hierarquia"""
    total_classes_per_level = [0 for i in range(max_level)]
    for i in range(len(possible_class_level)):
        total_classes_per_level[possible_class_level[i]-1] += 1
    
    return total_classes_per_level