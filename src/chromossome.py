import random as rand
from call_nbayes import *
from dataset import Dataset

class Chromosome:
    def __init__(self, training_filename: str, test_filename: str, population_size: int, usefullness: str, 
                 mandatory_leaf_node_prediction: str, children_id: int):
        self.dataset = Dataset(test_filename)
        self.population_size = population_size
        self.children_id = children_id
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

        self.chromosome_fitness = 0.0 

    def create_attributes_population(self):
        ordered_pop = [0] * len(self.dataset.get_dataset_attributes())
        attributes = self.dataset.get_dataset_attributes()
        attributes.pop(-1)

        while len(self.attributes_population) < self.population_size:
            rand_gene = rand.choice(attributes)
            rand_gene_index = attributes.index(rand_gene)
            if rand_gene not in self.attributes_population:
                self.attributes_population.append(rand_gene)
                self.attributes_population_index.append(rand_gene_index)
                ordered_pop[rand_gene_index] = self.attributes_population[-1]
        self.attributes_population = [gene for gene in ordered_pop if gene != 0]
        self.attributes_population_index.sort()

    def create_population(self):
        dataset = self.dataset.get_dataset_data()
        attributes_class = []
        for i in range(len(dataset)):
            temp = []
            for k in self.attributes_population_index:
                temp.append(dataset[i][k])
            temp.append(dataset[i][-1])
            self.population.append(temp)
            if dataset[i][-1] not in attributes_class:
                attributes_class.append(dataset[i][-1])

        #self.dataset.dataset_attribute_class = attributes_class #Allow only when some bug happens 
        
        


        self.dataset.save_children(self.attributes_population, self.population, self.children_id)
        self.children_path = f'./datasets/chromossome_{self.children_id}.arff'
        self.output_nbayes = f'./datasets/nbayes_chromossome_{self.children_id}.arff'

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
    
    def get_fitness(self) -> float:
        """ Call the Naive Bayes algorithm.

        Returns:
            float: return the fitness of the chromosome
        """
        self.chromosome_fitness = call_nbayes(self.usefullness, self.mandatory_leaf_node_prediction, 
                                              self.training_filename, self.children_path, self.output_nbayes)
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
    


    
