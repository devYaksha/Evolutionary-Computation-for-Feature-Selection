from genetic_operators import *
from preprocessing import *


class GeneticAlgorithm:
    """This class is responsible for the genetic algorithm.

    `Args:`
    - population_size: The size of the population.
    - num_attributes: The number of attributes that will be selected in each chromosome.
    - usefulness: If the GMNB algorithm will use the usefulness function.
    - mandatory_leaf_node_prediction: If the GMNB algorithm will use the mandatory leaf node prediction function.
    - training_filename: The path of the training file.
    - test_filename: The path of the test file.

    `Enconding:`
        - .arff files: UTF-8

    `Selection:`
        - Tournament Selection

    `Fitness:`
        - GMNB cross-validation (5 folds)

    `Crossover:`
        - Partially Mapped Crossover (PMX)

    ´Mutation´
        - Swap Mutation

    """

    def __init__(self, population_size, num_attributes, num_generations, usefulness, mandatory_leaf_node_prediction, training_filename, test_filename):

        operators = genetic_operators(training_filename)
        self.population = operators.create_population(population_size, num_attributes)




if __name__ == "__main__":
    print("\033[H\033[J")
    
    discretized_test = 'datasets/cellcyle/CellCycle_test_discretized.arff'
    discretized_train = 'datasets/cellcyle/CellCycle_train_discretized.arff'

    GA = GeneticAlgorithm(30, 10, 10, 'y', 'y', discretized_train, discretized_test)



    