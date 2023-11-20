from chromossome import Chromosome
from genetic_operators import *

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

        # Read and organize Dataset

        self.population_size = population_size
        self.num_attributes = num_attributes
        self.usefulness = usefulness
        self.mandatory_leaf_node_prediction = mandatory_leaf_node_prediction
        self.training_filename = training_filename
        self.test_filename = test_filename
        self.population = []
        self.population_fitness = []
        self.num_generations = num_generations
        
        # Start Genetic Algoritmh

        self.create_population()
        
        
        # Genetic Operators

        for i in range(self.num_generations):
            
            self.calculate_population_fitness()
            self.population = tournament(self.population, self.population_fitness, population_size)
            self.population = crossover(self.population, self.num_attributes)
            
            #mutation

    def create_population(self):
        for i in range(self.population_size):
            chromosome = Chromosome(
                self.training_filename, self.test_filename, self.num_attributes,
                self.usefulness, self.mandatory_leaf_node_prediction, len(self.population)
            )
            self.population.append(chromosome)
            chromosome.attributes_population_index.sort()

    def calculate_population_fitness(self):
        self.population_fitness = [chromosome.get_fitness() for chromosome in self.population]

    def get_population(self):
        return self.population

    def get_population_fitness(self):
        return self.population_fitness


if __name__ == "__main__":
    print("\033[H\033[J")
    k = GeneticAlgorithm(3, 2, 1, 'y', 'y', "./datasets/simple_treino.arff", "./datasets/simple_test.arff")
    #j = GeneticAlgorithm(3, 2, 'y', 'y', "./datasets/treino0.arff", "./datasets/teste0.arff")

    