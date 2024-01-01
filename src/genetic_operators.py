import random
import os

from utils import *
from dataset import Dataset
from cross_validation import *

class genetic_operators:

    def __init__(self, test_dataset_path) -> None:
        self.data = Dataset(test_dataset_path)
        self.filepath = test_dataset_path


    def create_population(self, population_size: int, num_attributes: int):
        """Create the initial population.

        `Args:`
            population_size (int): the size of the population
            num_attributes (int): the number of attributes that will be selected in each chromosome
        """

        attributes = self.data.dataset_attributes[:-1]
        if num_attributes > len(attributes):
            print(f'Warning: the number of attributes ({num_attributes}) is greater than the number of attributes in the dataset ({len(attributes)})')
            exit(1)

        for id in range(population_size):
            objects = []  # Initialize the list for each chromosome
            chromossome_attributes = random.sample(attributes, num_attributes)
            index_attributes = [attributes.index(attribute) for attribute in chromossome_attributes]

            # Sort index_attributes and use the sorted order to sort chromossome_attributes
            sorted_indices = sorted(range(len(index_attributes)), key=lambda k: index_attributes[k])
            index_attributes = [index_attributes[i] for i in sorted_indices]
            chromossome_attributes = [chromossome_attributes[i] for i in sorted_indices]

            for i in range(len(self.data.dataset_objects)):
                subset = [str(self.data.dataset_objects[i][j]) for j in index_attributes]
                subset.append(str(self.data.dataset_objects[i][-1]))  # Append the last element as a string
                objects.append(subset)

            chromossome_attributes.append(self.data.dataset_attributes[-1])
            temporary_chromossome = Dataset(self.filepath)
            temporary_chromossome.dataset_dict['description'] = ''
            temporary_chromossome.dataset_dict['attributes'] = chromossome_attributes
            temporary_chromossome.dataset_dict['data'] = objects
            temporary_chromossome.save_dataset(f'chromossome_{id}.arff')

            

    def evaluate_fitness(self, population_size, training_path, cross_validation_check = True) -> list:
        chromossomes_fitness = []
        if cross_validation_check:
            for id in range(population_size):
                chromossomes_fitness.append(cross_validation(f'chromossome_{id}.arff', training_path))
            return chromossomes_fitness
        
        for id in range(population_size):
            chromossomes_fitness.append(call_nbayes(training_path, f'chromossome_{id}.arff', (f'./result_{id}.txt')))
        return chromossomes_fitness
    
    def tournament_selection(self, population_size, fitness):

        winner_chance = 0.75

        for _ in range(population_size):
            fighters = random.sample(fitness, 2)
            index_fighters = [fighters.index(attribute) for attribute in fitness]
            print(fighters)
            print(index_fighters)


        pass
        






    

       


        


if __name__ == "__main__":
    os.system("clear")
    os.system("python3 src/genetic_algorithm.py")
        





