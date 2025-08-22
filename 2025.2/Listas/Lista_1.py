##Resolucao da Lista 1 de revisao de computacao 1

#--------------------------------------------

#Questão 1

# def calcular_combustivel(): 

#     for i in range(3):

#         x = 500, 300, 200
#         y = 10, 12, 8

#         print(x[i]/y[i])

# print(calcular_combustivel())

#Questão 2

# def verificar_tarefa():

#     while True:

#         lista = ["andar", "comer", "dormir"]
#         tarefa = (input("Digite a tarefa: "))

#         if tarefa in lista:
#             print("Esta na lista")
#         else:
#             print("Não esta na lista")

#         continuar = input("Deseja continar ? (s/n):").strip().lower()
#         if continuar != 's':
#             break

# print(verificar_tarefa())

#Questão 3

# def adiciona_item():

#     lista = ["arroz", "feijao", "leite"]
#     item = input("digite o item: ")

#     if item in lista:
#         print(f'{item} já tem na lista')
#     else:
#         lista.append(item)
#         print(lista)

# print(adiciona_item())

#Questão 4

# def contar_palavras():

#     lista_1 = ["maçã", "banana", "maçã", "laranja", "banana", "banana"]
#     lista_2 = []

#     for item in lista_1:
#         if item not in lista_2:
#             lista_2.append(item)
#             print(f'{item}: {lista_1.count(item)}')

# print(contar_palavras())

#Questão 5

# def classficiar_idade():

#     idade = int(input("Digite a idade: "))

#     if idade<12:
#         return "Criança"
#     elif idade <=17 and idade >= 12:
#         return "Adolescente"
#     elif idade <=64 and idade >= 18:
#         return "Adulto"
#     else:
#         return "Idoso"

# print(classficiar_idade())

#Questão 6

# def calcular_desconto():

#     valor = float(input("Digite o valor: "))
    
#     if valor <= 100:
#         desconto = valor * 0.05
#     elif valor <= 500 and valor > 100:
#         desconto = valor * 0.10
#     elif valor <+ 1000 and valor >500:
#         desconto = valor *0.15
#     else:
#         desconto = valor * 0.20

#     valor_final = valor - desconto
#     return f'R$ {valor_final}'

# print(calcular_desconto())

#Quesão 7

# def contagem_regressiva():

#     n = int(input("Insira um Número: "))

#     while n > 0:
#         print(n)
#         n -= 1
#     print("Fim da contagem!")

# print(contagem_regressiva())

#Quesão 8

# def classifica_estudantes():

#     notas = []
#     media = float(input("Digite a média: "))

#     for i in range(5):
#         nota = float(input(f"Digite a nota do estudante {i+1}: "))
#         notas.append(nota)

#         aprovados = []
#         reprovados = []

#     for i, nota in enumerate(notas):
#         if nota >= media:
#             aprovados.append(f"Estudante {i+1} aprovado com nota {nota}")
#         else:
#             reprovados.append(f"Estudante {i+1} reprovado com nota {nota}")
#     return {
#         "aprovado": len(aprovados),
#         "reprovado": len(reprovados)
#     }

# print(classifica_estudantes())

#Questao 9

# def verificar_acesso():
#     while True:
#         idade = int(input("Digite a idade: "))
#         if idade >= 18:
#             print("Acesso permitido a todas as atrações.")
#         else:
#             print('Acesso restrito às atrações para menores de idade.')
#         continuar = input("Deseja verificar o acesso para mais pessoas? (s/n): ").strip().lower()
#         if continuar != 's':
#             break

# print(verificar_acesso()) 

#Questão 10

# def verifica_senha():
#     tentativas = 0
#     while tentativas < 3:
#         senha = input("Digite a senha: ")
#         if len(senha) >= 8:
#             print("Senha aceita.")
#             return
#         else:
#             print("Senha inválida! Deve conter pelo menos 8 caracteres.")
#             tentativas += 1
#     print("Número de tentativas excedido.")

# print(verifica_senha())