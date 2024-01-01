from genetic_operators import *
from preprocessing import *


class GeneticAlgorithm:
    """This class is responsible for the genetic algorithm.

    `Args:`
    - population_size: The size of the population.
    - num_attributes: The number of attributes that will be selected in each chromosome.
    - training_filename: The path of the training file.
    - test_filename: The path of the test file.

    `Enconding:`
        - .arff files: UTF-8

    `Selection:`
        - Tournament Selection

    `Fitness:`
        - GMNB cross-validation (5 folds)

    `Crossover:`
        - Partially Mapped Crossover `PMX)

    `Mutation`
        - Swap Mutation

    """

    def __init__(self, population_size, num_attributes, num_generations, training_filepath, test_filepath):

        operators = genetic_operators(test_filepath)        
        operators.create_population(population_size, num_attributes)

        for _ in range(num_generations):
            chromossome_fitness = operators.evaluate_fitness(population_size, training_filepath, cross_validation_check = False)
            print(chromossome_fitness)
            
            #operators.tournament_selection(population_size, chromossome_fitness)



if __name__ == "__main__":
    print("\033[H\033[J")
    
    discretized_test = 'datasets/cellcyle/CellCycle_test_discretized.arff'
    discretized_train = 'datasets/cellcyle/CellCycle_train_discretized.arff'


    GA = GeneticAlgorithm(15, 10, 1, discretized_train, discretized_test)



    