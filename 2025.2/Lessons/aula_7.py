import math
import random
import numpy as np

print(math.sqrt(20))
print(math.log(10))
print(math.sin(math.radians(90)))

# ------------------------------------------------------

print(random.randint(1,10))
print(random.random())
itens = ['maçã', 'laranja', 'banana']
print(random.choice(itens))

x = print(random.randint(1,100))
print(math.sqrt(31))

# -------------------------------------------------------

x = np.array([1,2,3])
y = np.array([1.,0.,0.], [0.,1.,0.])
x
y
type(x)

array_zeros = np.zeros(5)
print(array_zeros)

matriz_zeros = np.zeros((3,4))
print(matriz_zeros)

array_1 = ([1,2,3])
array_2 = ([3,2,1])
print(array_1 + array_2)
print(array_1 * 2)

matriz = np.random.randint(1,11, size=(5,5))
somas_linhas = np.sum(matriz, axis=1)
print("matriz 5x5: ")
print(matriz)
print('Soma de cada linha')
print(somas_linhas)
