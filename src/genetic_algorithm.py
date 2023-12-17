import os
from chromossome import Chromosome
from genetic_operators import *
from preprocessing import *
from matpltlib import *

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

        #delete_old_childrens()

        self.population_size = population_size
        self.num_attributes = num_attributes
        self.usefulness = usefulness
        self.mandatory_leaf_node_prediction = mandatory_leaf_node_prediction
        self.training_filename = training_filename
        self.test_filename = test_filename

        self.best_fitness_global = float('-inf')
        self.best_chromossome = None # Object Chromossome

        self.population = [] # List of Chromossomes objects
        self.population_fitness = [0 for i in range(population_size)]
        self.num_generations = num_generations

        self.num_chromossomes = 0
        
        # Start Genetic Algoritmh
        os.system('clear')
        print("*** Starting Genetic Algorithm ***")
        self.create_population()
        
        # Genetic Operators
        best_fitness_per_generation = []
        average_arithmetic_fitness = []

        for i in range(self.num_generations):
            print(f"Generation {i+1}")
            print("\033[H\033[J")
            self.calculate_population_fitness()
            self.population = elitism(self.population, self.population_fitness)
            self.population = tournament(self.population, self.population_fitness, population_size//2)
            #self.population = crossover(self.population, self.num_attributes) #bugs
            

            #mutation

            average_arithmetic_fitness.append(sum(self.population_fitness)/len(self.population_fitness))
            best_fitness_per_generation.append(max(self.population_fitness))
            if max(self.population_fitness) > self.best_fitness_global:
                index = self.population_fitness.index(max(self.population_fitness))
                self.best_fitness = max(self.population_fitness)
                self.best_chromossome = self.population[index]


            #pause()
           
        plot_fitness(average_arithmetic_fitness)
        plot_fitness(best_fitness_per_generation)
        print("Best fitness Global: ", self.best_fitness_global)


   
    

    def create_population(self):
        for i in range(self.population_size):
            chromosome = Chromosome(
                self.training_filename, self.test_filename, self.num_attributes,
                self.usefulness, self.mandatory_leaf_node_prediction, self.num_chromossomes
            )
            self.population.append(chromosome)
            chromosome.attributes_population_index.sort()
            self.num_chromossomes += 1

    def calculate_population_fitness(self):
        self.population_fitness.clear()
        for i in range(len(self.population)):
            self.population_fitness.append(self.population[i].get_fitness())
            print(f"Chromossome {i} Fitness: {self.population_fitness[-1]}")

        if max(self.population_fitness) > self.best_fitness_global:
            self.best_fitness_global = max(self.population_fitness)


    def get_population(self):
        return self.population

    def get_population_fitness(self):
        return self.population_fitness



if __name__ == "__main__":
    print("\033[H\033[J")
    
    discretized_test = './datasets/cellcyle/CellCycle_test_DiscretizedData.arff'
    discretized_train = './datasets/cellcyle/CellCycle_train_DiscretizedData.arff'

    GA = GeneticAlgorithm(6, 10, 10, 'y', 'y', discretized_train, discretized_test)



    