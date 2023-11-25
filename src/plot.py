import matplotlib.pyplot as plt
import numpy as np

def plot_fitness(valores):
    indices = list(range(1, len(valores) + 1))
    fig, ax = plt.subplots()
    ax.plot(indices, valores, marker='o', linestyle='-')

    ax.set_xlabel('Generation')
    ax.set_ylabel('Fitness')
    ax.set_title('Fitness by Generation') 
    plt.show()



