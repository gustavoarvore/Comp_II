##Resolucao da Lista 1 de revisao de computacao 1

#--------------------------------------------

#Questão 1

#funcao que calcula o valor de 3 viagens com base em distancia e combustivel 
def calcular_combustivel(): 

    for i in range(3):

        x = 500, 300, 200
        y = 10, 12, 8

        print(x[i]/y[i])

print(calcular_combustivel())

#Questão 2

def verificar_tarefa():

    lista = ["andar", "comer", "dormir"]
    tarefa = (input("Digite a tarefa: "))

    if tarefa in lista:
        return "Esta na lista"
    else:
        return "Não esta na lista"

print(verificar_tarefa())

#Questão 3

def adiciona_item():

    lista_compras = []
    item = ...