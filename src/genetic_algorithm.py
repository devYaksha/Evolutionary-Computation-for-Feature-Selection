from population_manipulator import Attributes_ClassPopulation, AttributesPopulation
from genetic_operators import *
from dataset import *


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
        - Partially Mapped Crossover (PMX)

    `Mutation`
        - Swap Mutation

    """

    def __init__(self, population_size, num_generations, training_filepath, test_filepath, attributes_class = True, cross_validation = False) -> None:
        
        if attributes_class:
            population = Attributes_ClassPopulation(test_filepath)

        else:
            population = AttributesPopulation(test_filepath)

        operators = genetic_operators()   
        utils = Utils()
        utils.clear_screen()

        self.best_chromosome = (None, 0)
        self.fitness_history = []
        self.best_fitness_history = []

        #                                               #
        #                                               #
        #                                               #
        #                                               #
        #           Starting the Algorithm              #
        #                                               #
        #                                               #
        #                                               #
        #                                               #


        population_list = population.create_population(population_size)

        for generation in range(num_generations):
            
            population_fitness = population.evaluate_fitness(population_list, training_filepath, cross_validation_check = cross_validation)
            population_list = operators.tournament_selection(population_list, population_fitness)
            population_list = operators.pmx_crossover(population_list)
            population_list = operators.swap_mutation(population_list)

            utils.print_population_fitness(population_fitness, generation)

            if max(population_fitness) > self.best_chromosome[1]:
                index = population_fitness.index(max(population_fitness))
                self.best_chromosome = (population_list[index], population_fitness[index])      
                self.best_fitness_history.append(population_fitness[index])     


            self.fitness_history.append(sum(population_fitness) / len(population_fitness))

        print(f"\n\nBest Chromosome: {self.best_chromosome[0]}")
        print(f"Best Fitness: {self.best_chromosome[1]}")
        
        utils.plot_fitness_history(self.fitness_history)
        utils.plot_fitness_history(self.best_fitness_history, title = 'Best-Fitness History')




    