from organize_data import Dataset
from settings import *
from sklearn.preprocessing import KBinsDiscretizer
import numpy as np
import pandas as pd
import os

from scipy.io import arff
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedKFold




def discretize_data(dataset_path: str, output_path: str, preprocessing = True) -> None:
    """Discretize data using KBinsDiscretizer, and makes pre-processing of the data classes,
     removing classes with less than 10 instances with default

    `Args:`
    
        - dataset_path (str): the path of the dataset to be discretized
        - output_path (str): the path of the discretized dataset output
        - preprocessing (bool): if the data classes will be pre-processed.
        
    `Returns:`

        - A new dataset with the discretized data.
        
    """
    dataset = Dataset(dataset_path) # Create dataset object
    if preprocessing:
        new_attributes, new_dataset = dataset_preprocessing(dataset.get_dataset_attributes_class(), dataset.dataset_data) # Preprocess dataset
        dataset.set_dataset_attributes_class(new_attributes) # Set new attributes
        dataset.set_dataset_data(new_dataset)  # Set new dataset data

    attributes = dataset.get_dataset_attributes()
    data = dataset.get_dataset_data()
    float_data = []
    classes_data = []

    for i in range(len(data)):
        float_data.append([float(x) for x in data[i][:-1]]) # strings -> floats
        classes_data.append(data[i][-1]) # Add classes to lists

    # Discretize data using KBinsDiscretizer
    est = KBinsDiscretizer(n_bins=20, encode='ordinal', strategy='uniform', subsample=None)
    est.fit(float_data)
    discretized_data = est.transform(float_data)
    variance_per_feature = [int(value) for value in np.unique(discretized_data)]

    with open(output_path, 'w+') as file:
        file.write(f"{dataset.get_dataset_name()}-D\n")
        for attr in attributes:
            attr_name = attr.strip().split(' ')[1]
            attr_string = f"{attr_name} {{{','.join(map(str, variance_per_feature))}}}"
            file.write(f"@attribute {attr_string}\n")

        labels, label_list = assign_labels(dataset.get_dataset_attributes_class())
        file.write(f"@attribute class {{{','.join(labels)}}}\n")
        file.write('@data\n')

        # Write discretized data 
        for i in range(len(discretized_data)):
                row = discretized_data[i]

                
                row = [int(value) for value in row] # float -> int 

                if row[-1] in labels:
                    index = labels.index(row[-1])
                    row[-1] = label_list[index]

                if classes_data[i] in labels:
                    index = labels.index(classes_data[i])

                # string before join
                file.write(','.join(map(str, row)) + "," + labels[index] + '\n')

def assign_labels(categories:list):
    """Assign labels to each category

    `Args:`
        categories (list):  List of categories/labels

    `Returns:`
        tuple(list, list):  Tuple with two lists, the first one is the list of categories and the second one is the list of labels
    """
    label_list = [f"Label{i}" for i in range(1, len(categories) + 1)]
    return categories, label_list


def dataset_preprocessing(attributes_class, dataset, minimum_classes = 10, num_classes_removed = 0, 
                          
                          ):
    recursion_check = 0
    for i in range(len(attributes_class)):
        num_classes_i = 0
        for j in range(len(dataset)):
            if attributes_class[i] == dataset[j][-1]:
                num_classes_i += 1
                
        if num_classes_i < minimum_classes:
            temp = list(attributes_class[i].split('.'))
            temp.pop(-1)
            new_class = '.'.join(temp)
            #print(f"Removing {attributes_class[i]} {num_classes_i} classes to -> {new_class}") #Debug
            for k in range(len(dataset)):
                if attributes_class[i] == dataset[k][-1]:
                    dataset[k][-1] = new_class
            recursion_check += 1
            attributes_class[i] = new_class
            num_classes_removed += 1
        
    if recursion_check > 0:
        return dataset_preprocessing(attributes_class, dataset, minimum_classes, num_classes_removed=num_classes_removed)  
    else:
        print("Preprocessing done! number of classes removed: ", num_classes_removed, "\n")
        return attributes_class, dataset


def cross_validation(path_test: str, path_train: str):
    """Divide the dataset into 5 parts and save each part in a .arff file"""

    # Load datasets
    dataset_test = Dataset(path_test)
    data_list_test = dataset_test.get_dataset_data()
    dataset_train = Dataset(path_train)
    data_list_train = dataset_train.get_dataset_data()

    df_test = pd.DataFrame(data_list_test)
    df_train = pd.DataFrame(data_list_train)
    

    X_test = df_test.iloc[:, :-1]   # Separating the attributes and 
    y_test = df_test.iloc[:, -1]    # the classes for test dataset

    # Using StratifiedKFold to maintain class proportions during cross-validation for test dataset
    skf_test = StratifiedKFold(n_splits=5, random_state=42, shuffle=True)

    for i, (train_index_test, test_index_test) in enumerate(skf_test.split(X_test, y_test)):
        X_train_test, X_test_test = X_test.iloc[train_index_test], X_test.iloc[test_index_test]
        y_train_test, y_test_test = y_test.iloc[train_index_test], y_test.iloc[test_index_test]

        train_data_test = pd.concat([X_train_test, y_train_test], axis=1).astype(str).values.tolist()
        test_data_test = pd.concat([X_test_test, y_test_test], axis=1).astype(str).values.tolist()
        train_df_test = pd.DataFrame(train_data_test, columns=df_train.columns)
        test_df_test = pd.DataFrame(test_data_test, columns=df_test.columns)

        # Saving the DataFrames to .arff files
        train_df_test.to_csv(f'train_data_train_{i + 1}.arff', index=False,header=False)
        test_df_test.to_csv(f'test_data_test_{i + 1}.arff', index=False, header=False)




if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')

    cross_validation('datasets/cellcyle/CellCycle_test_DiscretizedData.arff', 'datasets/cellcyle/CellCycle_train_DiscretizedData.arff')