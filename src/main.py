import os

from genetic_algorithm import GeneticAlgorithm
from dataset import DatasetManipulator

"""

preprocessing = DatasetManipulator()
preprocessing.discretize_data(test_path, output_test_path)
preprocessing.discretize_data(train_path, output_train_path)

preprocessing.minimum_classes(output_test_path, output_test_path, minimum= 20)
preprocessing.minimum_classes(output_train_path, output_train_path, minimum= 20)



utils.pause()
utils.clear_screen()

"""

test_path = "exemples-datasets/test_test.arff"
train_path = "exemples-datasets/test_train.arff"

GeneticAlgorithm(population_size=30, num_generations=100, training_filepath=train_path, test_filepath=test_path, attributes_class=True, cross_validation = False)


# best solution: 

"""
Best Chromosome: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1]
Best Fitness: 53.93858337402344


"""