from organize_data import Dataset

class GeneticAlgorithm:
    def __init__(self, filename):
        self.dataset = Dataset(filename)

t1 = GeneticAlgorithm("datasets/simple_treino.arff")
#t2 = GeneticAlgorithm("datasets/treino1.arff")

print(t1.dataset.get_data_hash())

"""Example:

cromossomo = [1,1,0,0,0]
13,9,classeA
crossvalidation-5fold"""