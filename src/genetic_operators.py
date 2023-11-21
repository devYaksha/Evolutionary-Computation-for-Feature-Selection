import random
from chromossome import Chromosome
import os

def tournament(population_list:list,  fitness_list:list, fight_len=5, winner_chance=7.5):
    survivors = []
    #print(f"chromossomes = {population_list}")
    k = winner_chance

    for i in range(len(population_list)):
        fighters_fitness = []
        fighters = []
        for j in range(fight_len):
            index = random.randint(0, len(population_list)-1)
            fighters.append(population_list[index])
            fighters_fitness.append(fitness_list[index])

        best_chromossome = [fighters_fitness[0],0]
        worst_chromossome = [fighters_fitness[0],0]

        for i in range(len(fighters)):
            if fighters_fitness[i] >= best_chromossome[1]:
                best_chromossome = (fighters_fitness[i], i)

            elif fighters_fitness[i] < worst_chromossome[1]:
                worst_chromossome = (fighters_fitness[i],i)

        #print(f"best_chromossome, index = {best_chromossome}")
        #print(f"worst_chromossome, index = {worst_chromossome}")

        if random.random() < k:
            survivors.append(fighters[best_chromossome[1]])
        else:
            survivors.append(fighters[worst_chromossome[1]])
    
    #print(f"survivors = {survivors}")
    return survivors
    



def crossover(population_list:list, num_attributes:int):
    """
    Perform crossover (single-point crossover) on two parent individuals.

    """
    childrens = []

    for i in range(len(population_list)//2):        
        parent1 = random.choice(population_list)
        population_list.remove(parent1)
        parent2 = random.choice(population_list)
        population_list.remove(parent2)


        # Choose a random crossover point
        crossover_point = random.randint(0, min(len(parent1.get_attributes_population()), len(parent2.get_attributes_population())))
        
        #childrens classes
        offspring1 = Chromosome(parent1.get_training_filename(), parent1.get_test_filename(), num_attributes, parent1.get_usefulness(), parent1.get_mandatory_leaf_node_prediction(), parent1.children_id+1000)
        offspring2 = Chromosome(parent2.get_training_filename(), parent2.get_test_filename(), num_attributes, parent2.get_usefulness(), parent2.get_mandatory_leaf_node_prediction(), parent2.children_id+2000)

        offspring1.attributes_population = parent1.get_attributes_population()[:crossover_point] + parent2.get_attributes_population()[crossover_point:]
        offspring2.attributes_population = parent2.get_attributes_population()[:crossover_point] + parent1.get_attributes_population()[crossover_point:]
        
        offspring1.attributes_population_index = parent1.get_attributes_population_index()[:crossover_point] + parent2.get_attributes_population_index()[crossover_point:]
        offspring2.attributes_population_index = parent2.get_attributes_population_index()[:crossover_point] + parent1.get_attributes_population_index()[crossover_point:]

        for i in range(len(parent1.get_population())):
            offspring1.population.append(parent1.get_population()[i][:crossover_point] + parent2.get_population()[i][crossover_point:])
            offspring2.population.append(parent2.get_population()[i][:crossover_point] + parent1.get_population()[i][crossover_point:])

        childrens.append(offspring1)
        childrens.append(offspring2)

    return offspring1, offspring2



    


