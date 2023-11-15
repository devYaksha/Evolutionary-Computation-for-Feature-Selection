import random as rand
from call_nbayes import *
from organize_data import Dataset

class GeneticAlgorithm:
    def __init__(self, training_filename:str, test_filename:str, population_size:int, usefullness:str,mandatory_leaf_node_prediction:str):
        self.dataset = Dataset(test_filename)
        self.population_size = population_size
        
        self.num_children = 0
        self.output_nbayes = ""
        self.children_path = ""

        self.attributes_population = []
        self.attributes_population_index = []
        self.create_attributes_population()

        self.population = []
        self.create_population()
        

        call_nbayes(usefullness, mandatory_leaf_node_prediction, training_filename, self.children_path, self.output_nbayes)

    def create_attributes_population(self):
        
        while len(self.attributes_population) < self.population_size:
            rand_gene = rand.choice(self.dataset.get_dataset_attributes())
            rand_gene_index = self.dataset.get_dataset_attributes().index(rand_gene)
            if rand_gene not in self.attributes_population:
                self.attributes_population.append(rand_gene)
                self.attributes_population_index.append(rand_gene_index)

    def create_population(self):
        dataset = self.dataset.get_dataset_data()
        for i in range(len(dataset)):
            temp_population = []
            for k in range(dataset[i].__len__() - 1):
                if k in self.attributes_population_index:
                    temp_population.append(dataset[i][k])

            temp_population.append(dataset[i][-1])
            self.population.append(temp_population)

        self.dataset.save_children(self.attributes_population, self.population, self.num_children)

        self.children_path = f'./datasets/children_{self.num_children}.txt'
        self.output_nbayes = f'./datasets/output_nbayes_{self.num_children}.txt'

        self.num_children += 1

    def get_attributes_population(self):
        return self.attributes_population

    def get_attributes_population_index(self):
        return self.attributes_population_index
    
    def get_population(self):
        return self.population


if __name__ == "__main__":
    print("\033[H\033[J")

    #t2 = GeneticAlgorithm("./datasets/simple_treino.arff","./datasets/simple_test.arff", 2, 'y', 'y')
    call_nbayes('y','y', './datasets/simple_treino.arff', './datasets/children_0.txt', './datasets/output_nbayes_manual_test.txt')
    

    
