import os
from chromossome import Chromosome
from genetic_operators import *
from discretize_data import *
from call_nbayes import *
from plot import *

class GeneticAlgorithm:
    """This class is responsible for the genetic algorithm.

    Args:
    - population_size: The size of the population.
    - num_attributes: The number of attributes that will be selected in each chromosome.
    - usefulness: If the naive bayes algorithm will use the usefulness function.
    - mandatory_leaf_node_prediction: If the naive bayes algorithm will use the mandatory leaf node prediction function.
    - training_filename: The path of the training file.
    - test_filename: The path of the test file.
    """
    def __init__(self, population_size, num_attributes, num_generations, usefulness, mandatory_leaf_node_prediction, training_filename, test_filename):

        self.delete_old_childrens()

        self.population_size = population_size
        self.num_attributes = num_attributes
        self.usefulness = usefulness
        self.mandatory_leaf_node_prediction = mandatory_leaf_node_prediction
        self.training_filename = training_filename
        self.test_filename = test_filename
        self.population = []
        self.population_fitness = []
        self.num_generations = num_generations

        self.num_chromossomes = 0
        
        # Start Genetic Algoritmh
        print("Starting Genetic Algorithm")
        self.create_population()
        print("First-Population created")
        
        # Genetic Operators
        self.avarage_fitness = []
        for i in range(self.num_generations):
            
            self.calculate_population_fitness()
            
            self.population = tournament(self.population, self.population_fitness, population_size//2)
            self.population = crossover(self.population, self.num_attributes) #bugs
            self.population = elitism(self.population, self.population_fitness)

            #mutation

            self.avarage_fitness.append(sum(self.population_fitness)/len(self.population_fitness))
           
            
        plot_fitness(self.avarage_fitness)


   
    

    def create_population(self):
        for i in range(self.population_size):
            chromosome = Chromosome(
                self.training_filename, self.test_filename, self.num_attributes,
                self.usefulness, self.mandatory_leaf_node_prediction, self.num_chromossomes
            )
            self.population.append(chromosome)
            chromosome.attributes_population_index.sort()
            self.num_chromossomes += 1

    def delete_old_childrens(self):
        current_directory = "./datasets"
        files = os.listdir(current_directory)
        for file in files:
            if file.endswith('.arff') and (file.startswith('c') or file.startswith('o')) or file.startswith('n'):
                file_path = os.path.join(current_directory, file)
                os.remove(file_path)


    def calculate_population_fitness(self):
        self.population_fitness.clear()
        self.population_fitness = [chromosome.get_fitness() for chromosome in self.population]

    def get_population(self):
        return self.population

    def get_population_fitness(self):
        return self.population_fitness


if __name__ == "__main__":
    print("\033[H\033[J")
    
    discretized_test = './datasets/cellcyle/CellCycle_test_DiscretizedData.arff'
    discretized_train = './datasets/cellcyle/CellCycle_train_DiscretizedData.arff'

    GA = GeneticAlgorithm(4, 30, 80, 'y', 'y', discretized_train, discretized_test)



    