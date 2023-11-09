class GeneticAlgorithm:
    def __init__(self, filename):
        self.dataset, self.dataset_attributes, self.dataset_data = self.get_dataset_info(filename)
        self.dataset_name = self.dataset[0]
        self.dataset_attribute_class = self.dataset_attributes[-2]
        self.classes_data_hash = {}
        self.num_classes = 0
        self.num_features = 0

        self.organize_classes_data()
        self.organize_dataset_data()
        self.insert_data_on_hash()

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

    def organize_classes_data(self):
        temp_dataset_attributes = self.get_dataset_attributes_class()
        start, end = temp_dataset_attributes.find('{'), temp_dataset_attributes.find('}')
        temp_dataset_attributes = temp_dataset_attributes[start + 1:end].split(',')
        self.dataset_attribute_class = temp_dataset_attributes

        for i in self.dataset_attribute_class:
            self.add_node(i)

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

    def insert_data_on_hash(self):
        for data_row in self.dataset_data:
            self.add_edge(data_row[-1], data_row[:-1])

    def get_hash(self):
        return self.classes_data_hash


t1 = GeneticAlgorithm("./datasets/CellCycle/treino1.arff")
t2 = GeneticAlgorithm("./datasets/treino1.arff")

print(t1.classes_data_hash)
