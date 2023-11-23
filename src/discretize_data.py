from organize_data import Dataset
from sklearn.preprocessing import KBinsDiscretizer

def discretize_data(dataset_path: str, output_path: str, default_range: list = [-1, -0.5, 0, 0.5, 1]):
    # Load dataset
    dataset = Dataset(dataset_path)
    attributes = dataset.get_dataset_attributes()

    with open(output_path, 'w+') as file:
        # Write dataset name
        file.write(f"{dataset.get_dataset_name()}-D\n")

        # Write attribute information
        for attr in attributes:
            attr_name = attr.strip().split(' ')[1]

            if default_range != ["numeric"]:
                attr_string = f"{attr_name} {{{','.join(map(str, default_range))}}}"
            else:
                attr_string = f"{attr_name} numeric"

            file.write(f"@attribute {attr_string}\n")

        # Write class attribute information
        labels, label_list = assign_labels(dataset.get_dataset_attributes_class())
        file.write(f"@attribute class {{{','.join(label_list)}}}\n")
        file.write('@data\n')

        # Get dataset data
        data = dataset.get_dataset_data()
        float_data = []
        classes_data = []

        # Convert data to float
        for i in range(len(data)):
            float_data.append([float(x) for x in data[i][:-1]])
            classes_data.append(data[i][-1])

        # Discretize data using KBinsDiscretizer
        est = KBinsDiscretizer(n_bins=20, encode='ordinal', strategy='uniform', subsample=None)
        est.fit(float_data)
        discretized_data = est.transform(float_data)

        # Write discretized data to file
        for i in range(len(discretized_data)):
            row = discretized_data[i]
            if row[-1] in labels:
                index = labels.index(row[-1])
                row[-1] = label_list[index]

            if classes_data[i] in labels:
                index = labels.index(classes_data[i])
            file.write(','.join(map(str, row)) + "," + label_list[index] + '\n')

def assign_labels(categories):
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
