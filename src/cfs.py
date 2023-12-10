import numpy as np

#
# Este código foi desenvolvido para desempenhar diversas operações relacionadas à seleção de recursos 
# e análise de correlação no âmbito do aprendizado de máquina e da análise de dados. 
# As funcionalidades aqui apresentadas têm como objetivo avaliar as relações entre 
# distintas características dentro de um conjunto de dados, abrangendo tanto 
# atributos numéricos quanto categóricos.
# Isso inclui  classificação hierárquica de multi-rótulo.
#
# 15/10/2023 

def pearson_coeff(a:list, b: list) -> float:
    """
    Calculate the Pearson correlation coefficient between two vectors.

    Parameters:
    - a (list or numpy.ndarray): First vector.
    - b (list or numpy.ndarray): Second vector.

    Returns:
    - float: Pearson correlation coefficient.

    Raises:
    - ValueError: If the lengths of vectors 'a' and 'b' are not equal.
    - ValueError: If standard deviation of either vector is zero.
    """
    if len(a) != len(b):
        raise ValueError("Vectors 'a' and 'b' must have the same length.")

    mean_a, mean_b = np.mean(a), np.mean(b)
    dif_a, dif_b = np.subtract(a, mean_a), np.subtract(b, mean_b)
    mul = np.multiply(dif_a, dif_b)

    stdev_a, stdev_b = np.std(dif_a), np.std(dif_b)

    if stdev_a == 0 or stdev_b == 0:
        raise ValueError("Standard deviation of a vector is zero, leading to division by zero.")

    pearson = np.abs(np.sum(mul) / (stdev_a * stdev_b))

    if np.isnan(pearson):
        # Handle the case where the result is NaN (division by zero)
        pearson = 0.00000001

    return pearson

def pearson_coeff_cat_num(a:list, b:list) -> float:
    """
    Calculate the Pearson correlation coefficient between a categorical vector (a) and a numerical vector (b).

    Parameters:
    - a (list or numpy.ndarray): Categorical vector.
    - b (list or numpy.ndarray): Numerical vector.

    Returns:
    - float: Weighted sum of Pearson correlation coefficients for each category.

    Raises:
    - ValueError: If the lengths of vectors 'a' and 'b' are not equal.
    - ValueError: If standard deviation of the binary vector is zero for any category.
    """
    if len(a) != len(b):
        raise ValueError("Vectors 'a' and 'b' must have the same length.")

    tam = len(a)
    sum_result = 0.0

    # Calculate distinct values and their frequencies in the categorical vector
    dist = np.unique(a)
    freq = [a.count(d) for d in dist]

    for k in range(len(dist)):
        # Convert the categorical vector to a binary vector for each distinct value
        binary = [1 if x == dist[k] else 0 for x in a]

        # Calculate the Pearson correlation coefficient for the binary vector and the numerical vector
        try:
            pearson = np.abs(np.corrcoef(binary, b)[0, 1])
        except ZeroDivisionError:
            raise ValueError("Standard deviation of the binary vector is zero for a category, leading to division by zero.")

        # Update the weighted sum
        sum_result += (freq[k] / tam) * pearson

    return sum_result


def pearson_coeff_cat_cat(a:list, b:list) -> float:
    """
    Calculate the Pearson correlation coefficient between two categorical vectors.

    Parameters:
    - a (list or numpy.ndarray): First categorical vector.
    - b (list or numpy.ndarray): Second categorical vector.

    Returns:
    - float: Weighted sum of Pearson correlation coefficients for each combination of categories.

    Raises:
    - ValueError: If the lengths of vectors 'a' and 'b' are not equal.
    - ValueError: If standard deviation of the binary vectors is zero for any category combination.
    """
    if len(a) != len(b):
        raise ValueError("Vectors 'a' and 'b' must have the same length.")

    sum_result = 0.0

    # Calculate distinct values and their frequencies in both categorical vectors
    dist_a, freq_a = np.unique(a, return_counts=True)
    dist_b, freq_b = np.unique(b, return_counts=True)

    for k in range(len(dist_a)):
        # Convert the first categorical vector to a binary vector for each distinct value
        binary_a = [1 if x == dist_a[k] else 0 for x in a]

        for i in range(len(dist_b)):
            # Convert the second categorical vector to a binary vector for each distinct value
            binary_b = [1 if x == dist_b[i] else 0 for x in b]

            # Calculate the joint probability and Pearson correlation coefficient for the binary vectors
            try:
                prop = np.sum(np.logical_and(binary_a, binary_b)) / len(a)
                pearson = np.abs(np.corrcoef(binary_a, binary_b)[0, 1])
            except ZeroDivisionError:
                raise ValueError("Standard deviation of the binary vectors is zero for a category combination, leading to division by zero.")

            # Update the weighted sum
            sum_result += (prop * pearson)

    return sum_result


def possible_class_hierarchy(a_class, dist_class):
    """
    Create a vector of possible classes in the hierarchy.

    Parameters:
    - a_class (list): Vector of class instances.
    - dist_class (list): Vector of distinct class instances.

    Returns:
    - list: Vector of possible classes in the hierarchy.

    Note:
    The input vectors 'a_class' and 'dist_class' are assumed to contain strings representing class instances.

    Raises:
    - ValueError: If 'dist_class' is empty.
    """
    if not dist_class:
        raise ValueError("'dist_class' must not be empty.")

    possible_class = []
    
    # Iterate through distinct classes and create the vector of possible classes
    for class_instance in dist_class:
        aux_str = class_instance.split('.')
        level = len(aux_str)
        
        # Add superclasses of the class to 'possible_class' if not already in the vector
        for j in range(level):
            possible_c = ".".join(aux_str[:j+1])
            if possible_c not in possible_class:
                possible_class.append(possible_c)

    # Sort the vector of possible classes
    possible_class.sort()

    return possible_class


def a_class_to_vec(a_class, possible_class):
    """
    Create a matrix of possible classes (columns) and their occurrence (1) or absence (0) in the instances of the base (rows).

    Parameters:
    - a_class (list): Vector of class instances.
    - possible_class (list): Vector of possible classes in the hierarchy.

    Returns:
    - list: Matrix of occurrence with rows representing instances and columns representing possible classes.

    Note:
    The input vectors 'a_class' and 'possible_class' are assumed to contain strings representing class instances.

    Raises:
    - ValueError: If 'possible_class' is empty.
    """
    if not possible_class:
        raise ValueError("'possible_class' must not be empty.")

    occurrence = []

    # Iterate through instances and create the matrix of occurrence
    for class_instance in a_class:
        instance_vec = [0] * len(possible_class)
        aux_str = class_instance.split('.')
        level = len(aux_str)

        # Mark the occurrence of each superclass in the instance
        for j in range(level):
            current_c = ".".join(aux_str[:j + 1])
            position = possible_class.index(current_c)
            instance_vec[position] = 1

        occurrence.append(instance_vec)

    return occurrence


def correlation_fl_multilabel(class_vec, data, f_type):
    """
    Create a vector of correlation between all features of the base and the class attribute,
    considering each class of the hierarchy as a binary class.

    Parameters:
    - class_vec (list): Matrix of occurrence with rows representing instances and columns representing possible classes.
    - data (list): Matrix of features with rows representing instances and columns representing features.
    - f_type (list): Vector indicating the type of each feature (1 for numerical, 2 for categorical).

    Returns:
    - list: Vector of correlation values between each feature and the class attribute.

    Raises:
    - ValueError: If the lengths of 'class_vec' and 'data' are not equal.
    """
    if len(class_vec) != len(data):
        raise ValueError("Lengths of 'class_vec' and 'data' must be equal.")

    correlation = []
    tam_class_vec = len(class_vec[0])
    tam_features = len(data[0])

    for k in range(tam_features):
        feature = [row[k] for row in data]

        sum_correlation = 0

        if f_type[k] == 1:  # Numerical feature
            for i in range(tam_class_vec):
                label = [row[i] for row in class_vec]
                pearson = np.abs(np.corrcoef(feature, label)[0, 1])
                sum_correlation += pearson
        else:  # Categorical feature
            for i in range(tam_class_vec):
                label = [row[i] for row in class_vec]
                pearson = pearson_coeff_cat_num(feature, label)
                sum_correlation += np.abs(pearson)

        pearson_normal = sum_correlation / tam_class_vec
        correlation.append(pearson_normal)

    return correlation

def correlation_fl_hierarchical(class_vec, data, f_type, class_level, w_0, classes_per_level):
    """
    Create a vector of correlation between all features of the base and the class attribute, considering each class
    of the hierarchy as a binary class with a weight assigned to each class level.

    Parameters:
    - class_vec (list): Matrix of occurrence with rows representing instances and columns representing possible classes.
    - data (list): Matrix of features with rows representing instances and columns representing features.
    - f_type (list): Vector indicating the type of each feature (1 for numerical, 2 for categorical).
    - class_level (list): Vector indicating the level of each class in the hierarchy.
    - w_0 (float): Weight parameter.
    - classes_per_level (list): Vector indicating the number of classes at each level of the hierarchy.

    Returns:
    - list: Vector of correlation values between each feature and the class attribute.

    Raises:
    - ValueError: If the lengths of 'class_vec', 'data', 'f_type', and 'class_level' are not equal.
    """
    if len(class_vec) != len(data) or len(data[0]) != len(f_type) or len(f_type) != len(class_level):
        raise ValueError("Lengths of 'class_vec', 'data', 'f_type', and 'class_level' must be equal.")

    correlation = []
    tam_class_vec = len(class_vec[0])
    tam_features = len(data[0])

    # Calculate the total weight multiplied by the total number of classes per level in the hierarchy
    sum_weight = sum(pow(w_0, k+1) * classes_per_level[k] for k in range(len(classes_per_level)))

    for k in range(tam_features):
        feature = [row[k] for row in data]
        sum_correlation = 0

        if f_type[k] == 1:  # Numerical feature
            for i in range(tam_class_vec):
                label = [row[i] for row in class_vec]
                pearson = np.abs(np.corrcoef(feature, label)[0, 1])
                sum_correlation += pearson * pow(w_0, class_level[i])
        else:  # Categorical feature
            for i in range(tam_class_vec):
                label = [row[i] for row in class_vec]
                pearson = pearson_coeff_cat_num(feature, label)
                sum_correlation += np.abs(pearson) * pow(w_0, class_level[i])

        pearson_normal = sum_correlation / sum_weight
        correlation.append(pearson_normal)

    return correlation

def correlation_f_to_f_vec(data, f_type):
    """
    Create a matrix of correlation between all pairs of features in the base, considering the types of features.

    Parameters:
    - data (list): Matrix of features with rows representing instances and columns representing features.
    - f_type (list): Vector indicating the type of each feature (1 for numerical, 2 for categorical).

    Returns:
    - list: Matrix of correlation values between each pair of features.

    Raises:
    - ValueError: If the length of 'data' is not equal to the length of 'f_type'.
    """
    if len(data[0]) != len(f_type):
        raise ValueError("Length of 'data' must be equal to the length of 'f_type'.")

    correlation_matrix = []
    tam_features = len(data[0])

    for k in range(tam_features - 1):
        correlation = []
        for j in range(k + 1, tam_features):
            if f_type[k] == 1 and f_type[j] == 1:  # Numerical and numerical
                f1 = [row[k] for row in data]
                f2 = [row[j] for row in data]
                pearson = pearson_coeff(f1, f2)
                correlation.append(pearson)
            elif f_type[k] == 1 and f_type[j] == 2:  # Numerical and categorical
                f1 = [row[k] for row in data]
                f2 = [row[j] for row in data]
                pearson = pearson_coeff_cat_num(f2, f1)
                correlation.append(pearson)
            elif f_type[k] == 2 and f_type[j] == 1:  # Categorical and numerical
                f1 = [row[k] for row in data]
                f2 = [row[j] for row in data]
                pearson = pearson_coeff_cat_num(f1, f2)
                correlation.append(pearson)
            else:  # Categorical and categorical
                f1 = [row[k] for row in data]
                f2 = [row[j] for row in data]
                pearson = pearson_coeff_cat_cat(f1, f2)
                correlation.append(pearson)

        correlation_matrix.append(correlation)

    return correlation_matrix



def merit_cfs(s, correlation_ff_mat, correlation_fl_vec):
    """
    Calculate the merit function value for a given set of candidate attributes.

    Parameters:
    - s (list): Vector of candidate attributes.
    - correlation_ff_mat (list): Matrix of correlation values between each pair of features.
    - correlation_fl_vec (list): Vector of correlation values between each feature and the class attribute.

    Returns:
    - list: Vector containing the merit function value.

    Raises:
    - ValueError: If the length of 's' is not equal to the number of columns in 'correlation_ff_mat'.
    """
    tam_features = len(s)
    merit = []
    sum_correlation_ff = 0
    sum_correlation_fl = 0

    s.sort()

    for k in range(tam_features - 1):
        for j in range(k + 1, tam_features):
            sum_correlation_ff += correlation_ff_mat[s[k]][s[j] - s[k] - 1]

    for k in range(tam_features):
        sum_correlation_fl += correlation_fl_vec[s[k]]

    merit_denominator = np.sqrt(tam_features + (tam_features * (tam_features - 1) * sum_correlation_ff))
    
    if np.isnan(merit_denominator):
        merit_denominator = 0.00000001

    merit_value = (tam_features * sum_correlation_fl) / merit_denominator
    merit.append(merit_value)

    return merit


