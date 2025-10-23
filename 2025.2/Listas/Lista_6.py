# Exercicio 1

arq = open('nomes.txt', 'w')
for i in range(5):
    nome = input('Digite um nome: ')
    arq.write(nome + '\n')  
arq = open('nomes.txt', 'r')
for linha in arq:
    print(linha)  
arq.close()


# Questão 2

try:
    arq = open('dados.txt', 'r')
    for linha in arq:
        print(linha)
    arq.close()
except FileNotFoundError:
    print('Erro: Arquivo inexistente!')
except PermissionError:
    print('Erro: O programa não tem permissão para abrir o arquivo!')


# Questão 3

arq = open('texto.txt', 'w')
arq.write('Seu Zé: sim, fui...fui eu quem comeu o bolo - disse Zé com um tom de superioridade \nJoana: Ah não, Zé - com os olhos lacrimejando - eu guardei pra mim da festa da Tia Lucia \nQuando derrepente \nPOW!!! \nSurge Dona Eldineia com um dos pés sem o chinelo Havaiana \nDona Eldineia: POIS VOCÊ TRATE DE COMPRAR UM BOLO PRA ELA AGORA! - aos berros \nSeu Zé sentiu um frio nas costas e saiu correndo até a padaria da esquina.')
arq = open('texto.txt', 'r')
conteudo = arq.read()
palavras = conteudo.split()

num_linhas = len(linhas)
num_palavras = sum(len(conteudo.split()) for linha in arq)
num_caracteres = len(conteudo)

print(f'numero total de linhas: {num_linhas}')
print(f'numero total de palavras: {num_palavras}')
print(f'numero total de caracteres: {num_caracteres}')
arq.close()


# Questão 4

try:
    arq = open('', 'w')
    arq.write('seila')
    arq = open('', 'r')
    for linha in arq:
        print(linha)
    arq.close()
except FileNotFoundError:
    print('Erro: Arquivo não encontrado')
except ValueError:
    print('Erro: Linha não pode ser convertida para número')
