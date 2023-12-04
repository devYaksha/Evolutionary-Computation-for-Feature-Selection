import random
from chromossome import Chromosome

def elitism(population_list: list, fitness_list: list) -> list:
    """Perform elitism in 1 chromossome of the population.

    `Args:`
        population_list (list): the list of chromossomes
        fitness_list (list): the list of fitness of each chromossome

    `Returns:`
        list: a new population with the best chromossome of the previous population in a random position
    """

    elite_fitness = float('-inf')
    elite_index = 0
    max_local = (max(fitness_list))
    elite_index = fitness_list.index(max_local)
    elite_fitness = max_local
    
    rand_index = random.randint(0, len(population_list) - 1)
    population_list[rand_index] = population_list[elite_index]

    print(f"elite_fitness = {elite_fitness}, elite_index = {elite_index}, rand_index = {rand_index}")

    return population_list


def tournament(population_list:list,  fitness_list:list, winner_chance=7.5):
    survivors = []
    k = winner_chance
    fight_len = len(population_list)//2

    if fight_len < 2:
        print("fight_len < 2, make sure that population_list is greater than 4")
        return population_list

    for i in range(len(population_list)):
        fighters_fitness = []
        fighters = []
        for j in range(fight_len):
            index = random.randint(0, len(population_list)-1)
            fighters.append(population_list[index])
            fighters_fitness.append(fitness_list[index])

        best_chromossome = max(fighters_fitness)
        worst_chromossome = min(fighters_fitness)
        index_of_best_chromossome = fighters_fitness.index(best_chromossome)
        index_of_worst_chromossome = fighters_fitness.index(worst_chromossome)

        if random.random() < k:
            survivors.append(fighters[index_of_best_chromossome])
        else:
            survivors.append(fighters[index_of_worst_chromossome])

    
    return survivors
    



def crossover(population_list: list, num_attributes: int):
    """
    Perform crossover (single-point crossover) on two parent individuals.

    """
    childrens = []

    while len(population_list) > 1:
        parent1 = random.choice(population_list)
        population_list.remove(parent1)
        parent2 = random.choice(population_list)
        population_list.remove(parent2)

        # Choose a random crossover point
        crossover_point = random.randint(0, min(len(parent1.get_attributes_population()), len(parent2.get_attributes_population())))

        # Children classes
        offspring1 = Chromosome(parent1.get_training_filename(), parent1.get_test_filename(), num_attributes, parent1.get_usefulness(), parent1.get_mandatory_leaf_node_prediction(), parent1.children_id)
        offspring2 = Chromosome(parent2.get_training_filename(), parent2.get_test_filename(), num_attributes, parent2.get_usefulness(), parent2.get_mandatory_leaf_node_prediction(), parent2.children_id)

        offspring1.attributes_population = parent1.get_attributes_population()[:crossover_point] + parent2.get_attributes_population()[crossover_point:]
        offspring2.attributes_population = parent2.get_attributes_population()[:crossover_point] + parent1.get_attributes_population()[crossover_point:]

        offspring1.attributes_population_index = parent1.get_attributes_population_index()[:crossover_point] + parent2.get_attributes_population_index()[crossover_point:]
        offspring2.attributes_population_index = parent2.get_attributes_population_index()[:crossover_point] + parent1.get_attributes_population_index()[crossover_point:]

        for i in range(len(parent1.get_population())):
            offspring1.population.append(parent1.get_population()[i][:crossover_point] + parent2.get_population()[i][crossover_point:])
            offspring2.population.append(parent2.get_population()[i][:crossover_point] + parent1.get_population()[i][crossover_point:])

        childrens.append(offspring1)
        childrens.append(offspring2)

    return childrens





