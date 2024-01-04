from genetic_algorithm import GeneticAlgorithm
from dataset import DatasetManipulator

print("\033[H\033[J")
    
    
folder_path = '/home/yksh/Desktop/bases_particionadas'
output_train_path = f'{folder_path}/CellCycle/10-folds/fold0/CellCycle_train_discretized.arff'
output_test_path = f'{folder_path}/CellCycle/10-folds/fold0/CellCycle_test_discretized.arff'


preprocessing = DatasetManipulator()
preprocessing.discretize_data(output_test_path, output_test_path)
preprocessing.discretize_data(output_train_path, output_train_path)
                              
preprocessing.minimum_classes(output_test_path, output_test_path)
preprocessing.minimum_classes(output_train_path, output_train_path)

GeneticAlgorithm(population_size=5, num_generations=1, training_filepath=output_train_path, test_filepath=output_test_path)