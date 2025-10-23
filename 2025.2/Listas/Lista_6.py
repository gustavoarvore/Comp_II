# Exercicio 1

for i in range(5):
    arq = open('nomes.txt', 'w')
    arq.write(input('Digite um nome: '))
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
for linha in arq:
    print(linha)
arq.close()


# Questão 4

