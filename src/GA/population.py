import random as rand

from organize_data import Dataset

class GeneticAlgorithm:
    def __init__(self, filename:str, population_size:int):
        self.dataset = Dataset(filename)
        self.population_size = population_size
        
        self.attributes_population = []
        self.attributes_population_index = []
        self.create_attributes_population()

        self.population = []
        self.create_population()

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

    def get_attributes_population(self):
        return self.attributes_population

    def get_attributes_population_index(self):
        return self.attributes_population_index
    
    def get_population(self):
        return self.population

t1 = GeneticAlgorithm("datasets/simple_treino.arff", 2)
#t2 = GeneticAlgorithm("datasets/treino1.arff")

print("\033[H\033[J")
print(t1.get_attributes_population())
print(t1.get_attributes_population_index())
print(t1.get_population())