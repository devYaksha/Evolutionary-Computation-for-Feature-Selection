import random
import os
from dataset import Dataset

class genetic_operators:

    def __init__(self, training_dataset) -> None:
        self.data = Dataset(training_dataset)


    def create_population(self, population_size: int, num_attributes: int) -> list:
        """Create the initial population.

        `Args:`
            population_size (int): the size of the population
            num_attributes (int): the number of attributes that will be selected in each chromosome

        `Returns:`
            list: a list of Chromosome objects
        """

        pass

    

       


        


if __name__ == "__main__":
    os.system("python3 src/genetic_algorithm.py")
        





