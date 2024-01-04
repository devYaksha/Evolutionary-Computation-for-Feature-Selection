from genetic_algorithm import GeneticAlgorithm

print("\033[H\033[J")
    
    
folder_path = '/home/yksh/Desktop/bases_particionadas'
train_path = f'{folder_path}/SPO/10-folds/fold0/SPO_train.arff'
test_path = f'{folder_path}/SPO/10-folds/fold0/SPO_test.arff'

output_train_path = f'{folder_path}/SPO/10-folds/fold0/SPO_train_discretized.arff'
output_test_path = f'{folder_path}/SPO/10-folds/fold0/SPO_test_discretized.arff'

GA = GeneticAlgorithm(5, 1, output_train_path, output_test_path)