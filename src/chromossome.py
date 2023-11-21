import random as rand
from call_nbayes import *
from organize_data import Dataset

class Chromosome:
    def __init__(self, training_filename: str, test_filename: str, population_size: int, usefullness: str, mandatory_leaf_node_prediction: str, children_num: int):
        self.dataset = Dataset(test_filename)
        self.population_size = population_size
        self.children_id = children_num
        self.output_nbayes = ""
        self.children_path = ""
        self.attributes_population = []
        self.attributes_population_index = []
        self.population = []
        self.test_filename = test_filename
        self.training_filename = training_filename
        self.usefullness = usefullness
        self.mandatory_leaf_node_prediction = mandatory_leaf_node_prediction

        self.create_attributes_population()
        self.create_population()

        self.chromosome_fitness = 0.0 #tests only
        #self.chromosome_fitness = call_nbayes(usefullness, mandatory_leaf_node_prediction, training_filename, self.children_path, self.output_nbayes)

    def create_attributes_population(self):
        ordered_pop = [0] * len(self.dataset.get_dataset_attributes())
        while len(self.attributes_population) < self.population_size:
            rand_gene = rand.choice(self.dataset.get_dataset_attributes())
            rand_gene_index = self.dataset.get_dataset_attributes().index(rand_gene)
            if rand_gene not in self.attributes_population:
                self.attributes_population.append(rand_gene)
                self.attributes_population_index.append(rand_gene_index)
                ordered_pop[rand_gene_index] = self.attributes_population[-1]
        self.attributes_population = [gene for gene in ordered_pop if gene != 0]

    def create_population(self):
        dataset = self.dataset.get_dataset_data()
        for data_row in dataset:
            temp_population = [data_row[k] for k in self.attributes_population_index]
            temp_population.append(data_row[-1])
            self.population.append(temp_population)

        self.dataset.save_children(self.attributes_population, self.population, self.children_id)
        self.children_path = f'./datasets/chromossome_{self.children_id}.arff'
        self.output_nbayes = f'./datasets/output_nbayes_{self.children_id}.arff'

    def print_chromosome(self):
        print(f"Name: {self.dataset.dataset_name} - Chromosome {self.children_id}")
        for i in range(len(self.attributes_population)):
            print(f"{self.attributes_population[i]}")
        for i in range(len(self.population)):
            print(f"{self.population[i]}")

        print(f"Index List: {self.attributes_population_index}")

        print(f"test_filename = {self.test_filename}")
        print(f"training_filename = {self.training_filename}")
        print()


    def get_attributes_population(self):
        return self.attributes_population

    def get_attributes_population_index(self):
        return self.attributes_population_index
    
    def get_population(self):
        return self.population
    
    def get_fitness(self):
        return self.chromosome_fitness
    
    def get_chromossome_path(self):
        return self.children_path
    
    def get_output_nbayes(self):
        return self.output_nbayes
    
    def get_training_filename(self):
        return self.training_filename
    
    def get_test_filename(self):
        return self.test_filename
    
    def get_usefulness(self):
        return self.usefullness
    
    def get_mandatory_leaf_node_prediction(self):
        return self.mandatory_leaf_node_prediction
    


    
