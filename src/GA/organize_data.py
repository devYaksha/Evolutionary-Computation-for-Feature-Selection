class Dataset:

    def __init__(self, filename):
        self.dataset, self.dataset_attributes, self.dataset_data = self.get_dataset_info(filename)
        self.dataset_name = self.dataset[0]
        self.dataset_attribute_class = self.dataset_attributes[-2]
        self.num_classes = 0
        self.num_features = 0

        self.organize_classes_data()
        self.organize_dataset_data()

        self.dataset_attributes.remove('')
        self.dataset_attributes.pop(-1)

    def get_dataset_info(self, filename):
        try:
            with open(filename) as file:
                text, attributes, data = [], [], []
                get_data = False

                for line in file:
                    text.append(line)

                    if get_data:
                        data.append(line)
                    elif line.startswith('@data'):
                        get_data = True
                    elif line.startswith('@attribute'):
                        attributes.append(line)

                text = ''.join(text).split('\n')
                attributes = ' '.join(attributes).split('\n')
                data = ''.join(data).split('\n')

                return text, attributes, data
        except FileNotFoundError:
            print(f"Error Opening file {filename}")
            return None, None, None

    def organize_classes_data(self):
        temp_dataset_attributes = self.get_dataset_attributes_class()
        start, end = temp_dataset_attributes.find('{'), temp_dataset_attributes.find('}')
        temp_dataset_attributes = temp_dataset_attributes[start + 1:end].split(',')
        self.dataset_attribute_class = temp_dataset_attributes

    def organize_dataset_data(self):
        self.dataset_data = [line.split(',') for line in self.dataset_data]

    def add_node(self, node):
        if node not in self.classes_data_hash:
            self.classes_data_hash[node] = {}
            self.num_classes += 1

    def add_edge(self, data_class, value):
        self.classes_data_hash[data_class] = value
        self.num_features += 1 

    def get_dataset(self):
        return self.dataset

    def get_dataset_attributes(self):
        return self.dataset_attributes

    def get_dataset_data(self):
        return self.dataset_data

    def get_dataset_name(self):
        return self.dataset_name

    def get_dataset_attributes_class(self):
        return self.dataset_attribute_class

    def get_data_hash(self):
        return self.classes_data_hash
    
