import os
from call_nbayes import *

class Utils:

    def delete_chromossomes(self):
        current_directory = "./"
        files = os.listdir(current_directory)
        for file in files:
            if file.endswith('.arff') and (file.startswith('chromossome')):
                file_path = os.path.join(current_directory, file)
                os.remove(file_path)
                
                
    def pause(self):
        input("Press the <ENTER> key to continue...")


    def print_population_fitness(self, population_fitness, generation):
        best_fitness = max(population_fitness)
        worst_fitness = min(population_fitness)
        
        print(f"Generation {generation}: ")
        """
        for i in range(len(population_fitness)):
            print(f"Chromossome {i}: {population_fitness[i]}")
        print()
        """

        print(f"Best fitness: {best_fitness}")
        print(f"Worst fitness: {worst_fitness}")
        print(f'Difference: {best_fitness - worst_fitness}')
        print()
        print(f"Average fitness: {sum(population_fitness) / len(population_fitness)}")
        
        print()
    
