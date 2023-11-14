import math
from utils import *

def pearsonCoeff(vectorA:list, vectorB:list):
    """Calculate the Pearson correlation coefficient between two {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}al lists.

    Args:
        vectorA (list): a {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}al list. 
        vectorB (list): a {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}al list. 

    Returns:
        float: Return the Pearson correlation coefficient between two lists.
        - 1 = Correlation perfect positive
        - 0 = No correlation
    """    
    
    mean_A, mean_B = mean(vectorA), mean(vectorB)
    dif_A, dif_B = operatorMinus(vectorA, mean_A), operatorMinus(vectorB, mean_B)
    product_AB = sum_vc(operatorMultiplication(dif_A, dif_B))
    stdev_A, stdev_B = stdev(dif_A), stdev(dif_B)
    
    try:
        pearson = product_AB / (stdev_A * stdev_B)
    except ZeroDivisionError:
        return 0.00000001 
    
    return pearson


def pearsonCoeff_cat_num(vectorA:list, vectorB:list):
    """Calculate the Pearson correlation coefficient between a categorical list and a {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}al list.

    Args:
        vectorA (list): Categorical list.
        vectorB (list): {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}al list.

    Returns:
        float: Return the Pearson correlation coefficient between a categorical vector and a {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}al vector.
    """    

    size_vectorA = len(vectorA)
    vector_distinct = distinct(vectorA)
    frequence = frequence_double(vector_distinct, vectorA)

    pearson_sum = 0
    for i in range(len(vector_distinct)):
        binary = binaryVector(vector_distinct[i], vectorA)
        pearson = pearsonCoeff(binary, vectorB)
        pearson_sum += ((frequence[i]/size_vectorA)*abs(pearson))

    return pearson_sum 


def pearsonCoeff_cat_cat(vectorA:list, vectorB:list):
    """The Pearson correlation coefficient between two categorical vectors is calculated by the following formula:
    - r = sum(P(a,b)*|r(a,b)|), where:
    - P(a,b) = probability of the intersection between two vectors.
    - r(a,b) = Pearson correlation coefficient between two binary vectors.

    Args:
        vectorA (list): Categorical list.
        vectorB (list): Categorical list.

    Returns:
        float: Return the Pearson correlation coefficient between two categorical lists.
    """    

    sum_cat_cat = 0 
    pearson = 0
    dist_A, dist_B = distinct(vectorA), distinct(vectorB)
    
    for i in range(len(dist_A)):
        binary_A = binaryVector(dist_A[i], vectorA)
        
        for j in range(len(dist_B)):
            binary_B = binaryVector(dist_B[j], vectorB)
            probability = prob_a_and_b(binary_A, binary_B)
            pearson = pearsonCoeff(binary_A, binary_B)
            sum_cat_cat += (probability*abs(pearson))
    return sum_cat_cat


def possible_class_hierarchy(a_class:list, dist_class:list):
    """Iterates over the distinct classes and builds a vector of possible classes
    in the hierarchy. The result is sorted.

    Returns:
        list: A possible class hierarchy.
    """    

    possible_class = []
    concate = []
    for i in range(len(dist_class)):
        aux_str = explode(dist_class[i], '.')
        level = len(aux_str)

        for j in range(level):
            if j == 0:
                concate.append(aux_str[j])
            else:
                concate.append("." + aux_str[j])
            possible_c = concate[:]
            if in_array_string(possible_c, possible_class) == -1:
                possible_class.append(possible_c) #se for classe nova, adicona no vector possible_class

        
    possible_class.sort()
    return possible_class


def class_to_vector(a_class:list, possible_class:list):
    """receives a list of class instances and a list of possible class hierarchies.

    Returns:
        list: It generates a binary vector for each class instance, where each element in the vector corresponds
    to the presence (1) or absence (0) of a specific class hierarchy in 'possible_class'.
    """    

    occurrence = []
    for i in range(len(a_class)):
        instance_vec = [0]*len(possible_class)
        aux_str = explode(a_class[i], '.')
        for j in range(len(aux_str)):
            current_c = '.'.join(aux_str[:j + 1])
            position = in_array_string(current_c, possible_class)
            if position != -1:
                instance_vec[position] = 1
        occurrence.append(instance_vec)
    return occurrence


def correlation_fl_multilabel(class_vector:list, data:float, f_type):
    """Create a list of correlation between all features of the base and the class attribute, considering each class of the hierarchy as a binary class.

    Args:
        - class_vector (list): __
        -  data (float): 
        - f_type (?): 

    Returns:
        list: A list of correlation between all features of the base and the class attribute.
    """    

    correlation = []
    tam_class_vector = len(class_vector[0])
    tam_features = len(data[0])

    for k in range(tam_features):
        feature = get_column(data,k)
        sum_correlation = 0

        if f_type[k] == 1:
            for i in range(tam_class_vector):
                label = get_column(class_vector, i)
                pearson = pearsonCoeff(feature, label)
                sum_correlation += abs(pearson)

        else:
            for i in range(tam_class_vector):
                label = get_column(class_vector, i)
                pearson = pearsonCoeff_cat_num(feature, label)
                sum_correlation += abs(pearson)

        pearson_normal = sum_correlation/tam_class_vector
        correlation.append(pearson_normal)
        
    return correlation

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

def correlation_fl_hierarchical(class_vec, data, f_type, class_level, w_0, classes_per_level):
    tam_class_vec = len(class_vec[0])
    tam_features = len(data[0])
    sum_weight = 0
    correlation = []

    for k in range(len(classes_per_level)):
        sum_weight += (pow(w_0, k+1)*classes_per_level[k])

    for k in range(tam_features):
        feature = get_column(data,k)
        sum_correlation = 0

        if f_type[k] == 1:
            for i in range(tam_class_vec):
                label = get_column(class_vec, i)
                pearson = pearsonCoeff(feature, label)
                sum_correlation += abs(pearson)*(pow(w_0, class_level[i]))
        else: 
            for i in range(tam_class_vec):
                label = get_column(class_vec, i)
                pearson = pearsonCoeff_cat_num(feature, label)
                sum_correlation += abs(pearson)*(pow(w_0, class_level[i]))

        pearson_normal = sum_correlation/sum_weight
        correlation.append(pearson_normal)

    return correlation

def correlation_f_to_f_vec(data, f_type):
    correlation_matrix = []
    
    tam_features = len(data[0])
    
    for k in range(tam_features - 1):
        correlation = [] #reseta a cada iteração
        for j in range(k + 1, tam_features):
            if f_type[k] == 1 and f_type[j] == 1:  # {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}o e {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}o
                f1 = get_column(data, k)
                f2 = get_column(data, j)
                pearson = pearsonCoeff(f1, f2)
                correlation.append(pearson)
            elif f_type[k] == 1 and f_type[j] == 2:  # {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}o e categorico
                f1 = get_column(data, k)
                f2 = get_column(data, j)
                pearson = pearsonCoeff_cat_num(f2, f1)
                correlation.append(pearson)
            elif f_type[k] == 2 and f_type[j] == 1:  # categorico e {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}o
                f1 = get_column(data, k)
                f2 = get_column(data, j)
                pearson = pearsonCoeff_cat_num(f1, f2)
                correlation.append(pearson)
            else:  # categorico e categorico
                f1 = get_column(data, k)
                f2 = get_column(data, j)
                pearson = pearsonCoeff_cat_cat(f1, f2)
                correlation.append(pearson)
        
        correlation_matrix.append(correlation)
    
    return correlation_matrix



def merit_cfs(s, correlation_ff_mat, correlation_fl_vec):
    merit = []
    sum_correlation_ff = 0
    sum_correlation_fl = 0
    att_vec = s
    tam_features = len(att_vec)

    att_vec.sort()  # Atributos ordenados de maneira crescente

    for k in range(tam_features - 1):
        for j in range(k + 1, tam_features):
            sum_correlation_ff += correlation_ff_mat[att_vec[k]][att_vec[j] - att_vec[k] - 1]

    for k in range(tam_features):
        sum_correlation_fl += correlation_fl_vec[att_vec[k]]

    merit_denominator = pow((tam_features + (tam_features *(tam_features - 1) * sum_correlation_ff)), 0.5)

    if math.isnan(merit_denominator):
        merit_denominator = 0.00000001

    merit_value = (tam_features * sum_correlation_fl)/(merit_denominator)
    merit.append(merit_value)

    return merit


