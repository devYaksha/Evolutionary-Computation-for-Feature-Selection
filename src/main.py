from genetic_algorithm import GeneticAlgorithm
from dataset import DatasetManipulator
from call_nbayes import call_nbayes

#                                                                   
#                                                                   
#                                                                   
#                                                                   
#                  Main file to manipulate                 
#   The dataset and the genetic algorithm, and to find the best                                                                    
#                  attributes to be selected.                                                                     
#                                                                   
#                                                                   
#                                                                   

#You can change the paths here
test_path = "exemples-datasets/test_test.arff"
train_path = "exemples-datasets/test_train.arff"

# Preprocessing the dataset variables
discretize = False
set_minimum_classes = False
output_path_test = ""
output_path_train = ""
preprocessing = DatasetManipulator()

if discretize:
    preprocessing.discretize_data(test_path, output_path_test)
    preprocessing.discretize_data(train_path, output_path_train)


if set_minimum_classes:
    preprocessing.minimum_classes(output_path_test, output_path_test, minimum= 10)
    preprocessing.minimum_classes(output_path_train, output_path_train, minimum= 10)


# Genetic Algorithm variables
population_size = 10
num_generations = 5
cross_validation = False
GeneticAlgorithm(population_size, num_generations, train_path, test_path, cross_validation) # Genetic Algorithm object

# Call the nbayes algorithm with the best chromossome found
checking_best = call_nbayes(train_path, 'best_chromossome.arff')
print(f"Best Chromossome (checking fitness): {checking_best}")