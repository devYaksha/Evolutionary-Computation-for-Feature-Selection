import numpy as np
import pandas as pd
import os

from dataset import Dataset
from utils import *
from sklearn.preprocessing import KBinsDiscretizer
from sklearn.model_selection import StratifiedKFold
from call_nbayes import call_nbayes


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
        new_attributes, new_dataset = classes_preprocessing(dataset.get_dataset_attributes_class(), dataset.dataset_data) # Preprocess dataset
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
    """Assign labels to each category, helper function for discretize_data

    `Args:`
        categories (list):  List of categories/labels

    `Returns:`
        tuple(list, list):  Tuple with two lists, the first one is the list of categories and the second one is the list of labels
    """
    label_list = [f"Label{i}" for i in range(1, len(categories) + 1)]
    return categories, label_list


def classes_preprocessing(attributes_class, dataset,
                          minimum_classes = 10, num_classes_removed = 0):
    
    """ Remove classes with less than 10 instances or classes with only 'R' (root)
    
    During the preprocessing, if a class has less than 10 instances or is a root, it will be removed.
    
    if a class is removed, the function will be called again, until all classes have more than 10 instances.
    
    `Example:`
        - Class1: R.11.02.03.01 -> 5 instances
        - >> Class1: R.11.02.03 -> 7 instances
        - >> Class1: R.11.02 -> 9 instances
        - >> Class1: R.11 -> 12 instances
        
        
    `Args:`
        - attributes_class (list): list of attributes and classes
        - dataset (list): list of dataset data
        - minimum_classes (int): minimum number of classes to be removed
        - num_classes_removed (int): number of classes removed in the previous call of the function

    Returns:
        - None
    
    """
    
    
    recursion_check = 0
    root = False

    for i in range(len(attributes_class)):
        num_classes_i = 0

        for j in range(len(dataset)):

            if attributes_class[i] == 'R':
                root = True
                break

            elif attributes_class[i] == dataset[j][-1]:
                num_classes_i += 1


        if root:
            for object in dataset:
                if object[-1] == 'R':
                    print(f"Removing root") #Debug
                    dataset.remove(object) # Remove object with root from dataset                    


        elif num_classes_i < minimum_classes:
            temp = list(attributes_class[i].split('.'))
            temp.pop(-1)
            new_class = '.'.join(temp)
            print(f"Removing {attributes_class[i]} {num_classes_i} classes to -> {new_class}") #Debug
            for k in range(len(dataset)):
                if attributes_class[i] == dataset[k][-1]:
                    dataset[k][-1] = new_class
            recursion_check += 1
            attributes_class[i] = new_class
            num_classes_removed += 1
        
    if recursion_check > 0:
        return classes_preprocessing(attributes_class, dataset, minimum_classes, num_classes_removed=num_classes_removed)  
    else:
        for class_ in attributes_class:
            if class_ == 'R':
                print("Removing root in attributes_class") #Debug
                attributes_class.remove(class_)
                num_classes_removed += 1

        print("Preprocessing done! number of classes removed: ", num_classes_removed, "\n")
        return attributes_class, dataset


def five_folds(path_dataset: str, train=True) -> None:
    """Divide the dataset into 5 parts, and each part is saved in a .arff file.
    
    The dataset is divided using StratifiedKFold,
    to maintain class proportions during cross-validation.
    
    `Args:`
        - path_dataset (str): the path of the dataset to be discretized
        - train (bool): if the dataset is the train dataset or the test dataset, this is used to name the files.
        
    `Returns:`
        - A new dataset with the discretized data.
        
    
    """
    #
    dataset = Dataset(path_dataset)

    # Load datasets
    dataset_test = Dataset(path_dataset)
    data_list_test = dataset_test.get_dataset_data()

    df_test = pd.DataFrame(data_list_test)
    

    X_test = df_test.iloc[:, :-1]   # Separating the attributes and 
    y_test = df_test.iloc[:, -1]    # the classes for test dataset

    # Using StratifiedKFold to maintain class proportions during cross-validation for test dataset
    skf_test = StratifiedKFold(n_splits=5, random_state=42, shuffle=True)

    for i, (train_index_test, test_index_test) in enumerate(skf_test.split(X_test, y_test)):
        X_train_test, X_test_test = X_test.iloc[train_index_test], X_test.iloc[test_index_test]
        y_train_test, y_test_test = y_test.iloc[train_index_test], y_test.iloc[test_index_test]

        test_data_test = pd.concat([X_test_test, y_test_test], axis=1).astype(str).values.tolist()
        test_df_test = pd.DataFrame(test_data_test, columns=df_test.columns)
        
        # Saving the DataFrames to .arff files
        if train:
            test_df_test.to_csv(f'train_data_{i + 1}.arff', index=False, header=False)
            path = f'train_data_{i + 1}.arff'
        
        else:
            
            test_df_test.to_csv(f'test_data_{i + 1}.arff', index=False, header=False)
            path = f'test_data_{i + 1}.arff'


        fold_data = []
        with open(path, 'r') as file:
            for line in file:
                fold_data.append(line)
                fold_data[-1] = fold_data[-1].removesuffix('\n')


        dataset.save_fold(path, fold_data)

def cross_validation(dataset_test_path: str, dataset_train_path: str, num_folds = 5) -> None:
    """Make cross validation using the 5 parts of the dataset, with nbayes global model algorithm.
    
    `Args:`
        - dataset_test_path (str): the path of the test dataset (chromosome)
        - dataset_train_path (str): the path of the train dataset 
        
    `Returns:`
        - None    
    """

    five_folds(dataset_test_path, train=False)
    five_folds(dataset_train_path)
    sum_nbayes = 0 
    sum_itearation = 0
    
    for i in range(num_folds):
        print(f"Test {i + 1}:", end=" ")
        for j in range(num_folds):
            if i != j:
                print(f"Training {j + 1}", end=" -> ")
                sum_itearation += call_nbayes(f'train_data_{j + 1}.arff', f'test_data_{i + 1}.arff', f'result.arff')
        print()

        sum_itearation /= num_folds
        sum_nbayes += sum_itearation

    sum_nbayes /= num_folds

    
    
    current_directory = os.getcwd()
    for filename in os.listdir(current_directory): # Delete the files created by five_folds function
        if filename.startswith("train_data") or filename.startswith("test_data") or filename.startswith("result"):
            file_path = os.path.join(current_directory, filename)
            os.remove(file_path)
            #print(f"Deleted: {file_path}")

    print(f"nbayes cross validation: {sum_nbayes}")

    return sum_nbayes



if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    
    #Example of use of the functions

    dataset_test_path = 'datasets/cellcyle/CellCycle_test_DiscretizedData.arff' # Discretized dataset
    dataset_train_path = 'datasets/cellcyle/CellCycle_train_DiscretizedData.arff' # Discretized dataset 
    
    ### Classes preprocessing ###

    """
    chro = Dataset(dataset_train_path) # Create dataset object
    att_class, data = classes_preprocessing(chro.get_dataset_attributes_class(), chro.dataset_data) # Preprocess dataset
    chro.set_dataset_attributes_class(att_class) # Set new attributes
    chro.save_children(chro.dataset_attributes, data, 0) # Save file with the new dataset

    pause()

    """
    ### Cross validation ###

    os.system('cls' if os.name == 'nt' else 'clear')

    x = call_nbayes(dataset_train_path, dataset_test_path, 'result.arff') # Call nbayes global model algorithm to compare with cross validation
    cross_validation(dataset_test_path, dataset_train_path) # Call cross validation function
    print(f'nbayes global model: {x}')

    