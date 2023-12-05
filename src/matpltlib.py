import matplotlib.pyplot as plt
import numpy as np

def plot_fitness(valores, title = 'Fitness by Generation', x_label = 'Generation', y_label = 'Fitness'):
    indices = list(range(1, len(valores) + 1))
    fig, ax = plt.subplots()
    ax.plot(indices, valores, marker='o', linestyle='-')

    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title) 
    plt.show()



