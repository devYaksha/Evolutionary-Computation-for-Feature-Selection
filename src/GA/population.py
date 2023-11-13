from organize_data import Dataset

class GeneticAlgorithm:
    def __init__(self, filename):
        self.dataset = Dataset(filename)

t1 = GeneticAlgorithm("datasets/treino1.arff")
t2 = GeneticAlgorithm("datasets/treino1.arff")

print(t2.dataset.get_dataset_name())
print(t2.dataset.get_data_hash())