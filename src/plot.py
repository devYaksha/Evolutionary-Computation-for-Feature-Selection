import matplotlib.pyplot as plt

def plot_reta(lista):
    # Criar uma lista de índices para usar como eixo x
    indices = list(range(1, len(lista) + 1))

    # Criar uma figura e eixo
    fig, ax = plt.subplots()

    # Criar um gráfico de linha
    ax.plot(indices, lista, marker='o', linestyle='-')

    # Definir rótulos e título
    ax.set_xlabel('Índice')
    ax.set_ylabel('Valores da Lista')
    ax.set_title('Gráfico de Reta')

    # Inverter o eixo y para que a linha vá para cima com valores maiores
    ax.invert_yaxis()

    # Exibir o gráfico
    plt.show()

