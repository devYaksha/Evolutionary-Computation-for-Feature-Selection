from organize_data import Dataset
from sklearn.preprocessing import KBinsDiscretizer
import numpy as np

def discretize_data(dataset_path: str, output_path: str) -> None:
    """Discretize data using KBinsDiscretizer"""
    dataset = Dataset(dataset_path)
    attributes = dataset.get_dataset_attributes()

    # Get dataset data
    data = dataset.get_dataset_data()
    float_data = []
    classes_data = []

    
    for i in range(len(data)):
        float_data.append([float(x) for x in data[i][:-1]]) # List of str -> floats
        classes_data.append(data[i][-1])

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

                
                row = [int(value) for value in row] # Float -> int 

                if row[-1] in labels:
                    index = labels.index(row[-1])
                    row[-1] = label_list[index]

                if classes_data[i] in labels:
                    index = labels.index(classes_data[i])

                # string before join
                file.write(','.join(map(str, row)) + "," + labels[index] + '\n')

def assign_labels(categories:list):
    """Assign labels to each category

    Args:
        categories (list):  List of categories/labels

    Returns:
        tuple(list, list):  Tuple with two lists, the first one is the list of categories and the second one is the list of labels
    """
    label_list = [f"Label{i}" for i in range(1, len(categories) + 1)]
    return categories, label_list

if __name__ == "__main__":
    print("\033[H\033[J")
    
    dataset_test = './datasets/cellcyle/CellCycle_test.arff'
    discretized_test = './datasets/cellcyle/CellCycle_test_DiscretizedData.arff'
    dataset_train = './datasets/cellcyle/CellCycle_train.arff'
    discretized_train = './datasets/cellcyle/CellCycle_train_DiscretizedData.arff'

    discretize_data(dataset_test, discretized_test)
    discretize_data(dataset_train, discretized_train)

    
