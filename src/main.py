import os

from genetic_algorithm import GeneticAlgorithm
from dataset import DatasetManipulator
from utils import Utils


utils = Utils()
utils.clear_screen() 
    
folder_path = '/home/yksh/Desktop/bases_particionadas'
test_path = f'{folder_path}/CellCycle/10-folds/fold0/CellCycle_test.arff'
output_test_path = f'{folder_path}/CellCycle/10-folds/fold0/CellCycle_test_discretized.arff'

train_path = f'/home/yksh/Desktop/bases_completas/CellCycle_single.arff'
output_train_path = '/home/yksh/Desktop/bases_completas/CellCycle_Single_discretized.arff'

preprocessing = DatasetManipulator()
preprocessing.discretize_data(test_path, output_test_path)
preprocessing.discretize_data(train_path, output_train_path)

preprocessing.minimum_classes(output_test_path, output_test_path, minimum= 20)
preprocessing.minimum_classes(output_train_path, output_train_path, minimum= 20)

utils.pause()
utils.clear_screen()

GeneticAlgorithm(population_size=5, num_generations=1, training_filepath=output_train_path, test_filepath=output_test_path)