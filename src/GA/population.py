def create_genes(filename):
    try:
        file = open(filename)
    except:
        print(f"Error Opening file {filename}")
        return
    
    text = []
    for i in file:
        text.append(i)

    text = ''.join(text)
    text = text.split('\n')

    for i in range(0,len(text)-2):
        print(f'Gene {i+1}: {text[i]}')

create_genes('./datasets/treino1.arff')