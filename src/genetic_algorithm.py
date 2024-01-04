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

    def __init__(self, population_size, num_generations, training_filepath, test_filepath) -> None:
        
        operators = genetic_operators(test_filepath)   
        utils = Utils()


        #                                               #
        #                                               #
        #                                               #
        #                                               #
        #           Starting the Algorithm              #
        #                                               #
        #                                               #
        #                                               #
        #                                               #


        operators.create_population(population_size)

        for generation in range(num_generations):

            chromossome_fitness = operators.evaluate_fitness(population_size, training_filepath, cross_validation_check = False)
            utils.print_population_fitness(chromossome_fitness, generation)
            

        utils.delete_chromossomes()





    