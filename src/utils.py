import os
import matplotlib.pyplot as plt

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


    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')


    def plot_fitness_history(self, fitness_history, title = 'Avarage-Fitness History'):
        """
        Plot the fitness history.

        Parameters:
        - fitness_history (list): List containing fitness scores for each generation.
        """
        # Plotting the fitness history
        plt.plot(range(1, len(fitness_history) + 1), fitness_history, marker='o', linestyle='-')
        plt.title(title)
        plt.xlabel('Generation')
        plt.ylabel('Fitness Score')
        plt.grid(True)
        plt.show()
    
