# Importando a biblioteca necessária; Matplolib como plt
import matplotlib.pyplot as plt

# Criar um dataset com notas de alunos em uma lista
# Definindo os valores do eixo-x
notas = [10, 2, 8, 9, 5, 4, 7, 6, 8, 8, 4, 9, 9, 7, 9]

# Criar o histograma
plt.hist(notas, bins=10, color='c') 

# Adicionar os rótulos(labels)
plt.xlabel('Notas')
plt.ylabel('Frequencia')
plt.title('Exemplo de Histograma')

# Exibir o histograma
plt.show()
