# Para escrever dentro do arquivo
arq = open('arq_teste.txt', 'w')
arq.write('hello world')
arq.close()

# Apenas para leitura do arquivo
arq = open('arq_teste.txt', 'r')
info = arq.read()
print(info)
arq.close()

# Lendo o arquivo linha por linha
arq = open('arq_teste.txt', 'w')
arq.write('Oi /nVc q ta lndo /nnão fode')
arq = open('arq_teste.txt', 'r')
for linha in arq:
    print(linha)
arq.close()

# Retornando ao inicio de um arquivo
arq = open('arq_teste.txt', 'w')
arq.write('Oi /nVc q ta lndo /nnão fode')
arq = open('arq_teste.txt', 'r')
for linha in arq:
    print(linha)
arq.seek(0)
arq.close()

# FileNotFoundError
try:
    arq = open('arq_teste.txt', 'r')
    conteudo = arq.read()
except FileNotFoundError:
    print('Erro: O arquivo não foi encontrado!')

# IOError
try:
    arq = open('arq_teste.txt', 'w')
    conteudo = arq.read()
except IOError:
    print('Erro: Deu ruim!')

