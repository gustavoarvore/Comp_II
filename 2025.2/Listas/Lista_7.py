import random
import math
import numpy as np

#Questão 1
def dado():
    total = 0
    for _ in range(100):
        total += random.randint(1, 6)
    return total

resultado = dado()
print(f'A soma dos 100 lancamentos eh: {resultado}')


#Questão 2
matriz = np.zeros((4, 4))
np.fill_diagonal(matriz, 1)
print(matriz)


#Questão 3
matriz = np.ones((3, 3)) 
print(matriz *5)


#Questão 4
matriz = np.empty(2,3)
for i in range(2):
    for j in range(3):
        matriz[i,j] = input(f'digite um valor para i: {i} e para j: {j}')
print(matriz)


#Questão 5

class ArrayNumpy:
    def __init__(self):
        self.array = None
        
    def criar_zeros(self, shape):
        self.array = np.zeros(shape)
        return self.array
    
    def criar_uns(self, shape):
        self.array = np.ones(shape)
        return self.array
    
    def criar_vazios(self, shape):
        self.array = np.empty(shape)
        return self.array
    
    def mostrar_array(self):
        if self.array is not None:
            print(self.array)
        else:
            print("Nenhum array foi criado ainda.")