import numpy as np

from sklearn.preprocessing import KBinsDiscretizer
from dataset import Dataset
from utils import *

def discretize_data(dataset_path: str, output_path: str) -> None:
    """Discretize data using KBinsDiscretizer

    `Args:`
    
        - dataset_path (str): the path of the dataset to be discretized
        - output_path (str): the path of the discretized dataset output
        
    `Returns:`

        - A new dataset with the discretized data.
        
    """
    dataset = Dataset(dataset_path) # Create dataset object

    attributes = dataset.dataset_attributes # Get dataset attributes
    data = dataset.dataset_objects
    
    float_data = []
    classes_data = []

    for i in range(len(data)):
        float_data.append([float(x) for x in data[i][:-1]]) # strings -> floats
        classes_data.append(data[i][-1]) # Add classes to lists
 
    # Discretize data using KBinsDiscretizer
    est = KBinsDiscretizer(n_bins=20, encode='ordinal', strategy='uniform', subsample=None)
    est.fit(float_data)
    discretized_data = est.transform(float_data)
    variance_per_feature = list([int(value) for value in np.unique(discretized_data)])
    variance_per_feature = list([str(value) for value in variance_per_feature])

    data = discretized_data.tolist()


    for i in range(len(discretized_data)):
        data[i] = [int(x) for x in data[i]] # floats -> strings
        data[i].append(classes_data[i]) # Add classes to discretized data

    for j in range(len(attributes)):
        if attributes[j][0].upper() == 'CLASS':
            break
        
        attributes[j] = (attributes[j][0], variance_per_feature)
        
    dataset.dataset_dict['attributes'] = attributes # Update dataset attributes
    dataset.dataset_dict['data'] = data # Update dataset data

    dataset.save_dataset(output_path) # Save the dataset in a new file
    

def classes_preprocessing(dataset_path: str, output_path: str) -> None:
    
    """ Remove classes with less than 10 instances or classes with only 'R' (root)
    
    if a class is removed, the function will be called again, until all classes have more than 10 instances.
    
    """

    dataset = Dataset(dataset_path) # Create dataset object

    attributes_class = dataset.dataset_attributes[-1] # Get dataset attributes
    dataset_objects = dataset.dataset_objects
    count = 0
    minimum_classes = 10
    recursion_check = False

    # Remove 'R' from attributes_class[1]
    filtered_attributes = [attribute for attribute in attributes_class[1] if attribute != 'R']

    # Create a new list without objects having 'R'
    filtered_objects = [object for object in dataset_objects if object[-1] != 'R']

    # Update dataset_objects with the filtered list
    dataset_objects = filtered_objects
    attributes_class = (attributes_class[0], filtered_attributes)

    for i in range(len(attributes_class[1])):
        for j in range(len(dataset_objects)):
            
            if dataset_objects[j][-1] == attributes_class[1][i]:
                count += 1
    
        if count < minimum_classes:
            new_attribute = attributes_class[1][i].split('.')
            new_attribute.pop()
            new_attribute = '.'.join(new_attribute)

            print(f"Changing class {attributes_class[1][i]} with {count} instances to -> {new_attribute}")

            for j in range(len(dataset_objects)):
                if dataset_objects[j][-1] == attributes_class[1][i]:
                    dataset_objects[j][-1] = new_attribute

            attributes_class[1][i] = new_attribute
            recursion_check = True


    dataset.dataset_dict['attributes'][-1] = attributes_class
    dataset.dataset_dict['data'] = dataset_objects
    dataset.save_dataset(output_path)

    if recursion_check:
        classes_preprocessing(output_path, output_path)
    


#
#   Usage
#

if __name__ == "__main__":
    discretize_data("datasets/cellcyle/CellCycle_test.arff", "./datasets/test_test.arff")
    discretize_data("datasets/cellcyle/CellCycle_train.arff", "./datasets/test_train.arff")
    classes_preprocessing("./datasets/test_train.arff", "./datasets/test_train.arff")
    classes_preprocessing("./datasets/test_test.arff","./datasets/test_test.arff")

    pass