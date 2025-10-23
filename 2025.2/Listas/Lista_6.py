# Exercicio 1

arq = open('nomes.txt', 'w')
arq.write('Gustavo \nLucas \nMatheus \nMaria \nLarissa')
arq = open('nomes.txt', 'r')
info = arq.read()
print(info)
arq.close()