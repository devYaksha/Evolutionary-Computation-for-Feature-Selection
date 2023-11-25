class Dataset:

    def __init__(self, filename):
        #print(f"Organizing Dataset {filename}")
        self.dataset, self.dataset_attributes, self.dataset_data = self.get_dataset_info(filename)

        try:
            self.dataset.remove('')
            self.dataset_attributes.remove('')
            self.dataset_data.remove('')
            

        except Exception as e:
            pass

        finally:
            #print(f"Dataset: {self.dataset_attributes[-1]}")
            self.dataset_name = self.dataset[0]
            self.dataset_attribute_class = self.dataset_attributes[-1]
            
            self.num_classes = 0
            self.num_features = 0

            self.organize_classes_data()
            self.organize_dataset_data()

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

    def save_children(self,attributes_population:list, population:list, num_children:int):
            with open(f'./datasets/chromossome_{num_children}.arff', 'w+') as file:
                file.write(self.get_dataset_name() + '\n')
                for i in range(len(attributes_population)):
                    file.write(attributes_population[i] + '\n')

                attribute_str = ["@attribute class {"]
                temp = self.get_dataset_attributes_class()

                for item in temp:
                    if item != '{' and item != '}':
                        attribute_str.append(item)
                        attribute_str.append(',')


                attribute_str[-1] = '}'
                attribute_str = ''.join(attribute_str)
                file.write(attribute_str + '\n')
                file.write('@data\n')
                for j in range(len(population)):
                    for k in range(len(population[j])):
                        file.write(population[j][k])
                        if k != len(population[j]) - 1:
                            file.write(',')
                    file.write('\n')


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

