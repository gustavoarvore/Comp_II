#Questão: Sistema de Temperatura

# class termometro:
#     def __init__(self, temperatura):
#         self.temperatura = float(temperatura)

#     def converter_fahrenheit(self):
#         return (self.temperatura * 9/5 + 32)

#     def converter_kelvin(self):
#         return (self.temperatura + 273.15)

#     def verificar_estado(self):
#         if self.temperatura < 0:
#             return "Sólido"
#         elif self.temperatura >= 0 and self.temperatura <= 100:
#             return "Líquido"
#         else:   
#             return "Gasoso"

# termometro1 = termometro(input("Digite a Temperatura: "))
# print(f'A temperatura em Fahrenreit é {termometro1.converter_fahrenheit()}°F')
# print(f'A temperatura em Kelvin é {termometro1.converter_kelvin()}°K')
# print(f'O estado da água nessa temperatura é {termometro1.verificar_estado()}')

#Questão: Estudante

# class estudante:
#     def __init__(self, nome, nota1, nota2, nota3, media=0):
#         self.nome = nome
#         self.nota1 = float(nota1)
#         self.nota2 = float(nota2)
#         self.nota3 = float(nota3)
#         self.media = float(nota1+nota2+nota3)

#     def calcular_media(self):
#         return (self.media/3)

#     def verificar_aprovacao(self):
#         if self.calcular_media() >= 7:
#             print(f"O(A) Aluno(a) {self.nome} foi Aprovado(a) com média {self.calcular_media()}")
#         else:
#             print(f"O(A) Aluno(a) {self.nome} foi Reprovado(a) com média {self.calcular_media()}")
            
#     def atualizar_notas(self, nota1_1, nota2_2, nota3_3):
#         self.nota1_1 = nota1_1
#         self.nota2_2 = nota2_2
#         self.nota3_3 = nota3_3
#         print(f'Notas Atualizadas: {self.nota1_1}, {self.nota2_2}, {self.nota3_3}\n')
    
#     def mostrar_dados(self):
#         print(f'Nome: {self.nome}, Notas: {self.nota1}, {self.nota2}, {self.nota3}, Média: {self.calcular_media()}')

# estudante1 = estudante("Gustavo", 2, 6.5 ,8)
# print(f'A média do aluno é: {estudante1.calcular_media()}')
# estudante1.verificar_aprovacao()
# estudante1.mostrar_dados()
# estudante1.atualizar_notas(2,4,5)

# estudante2 = estudante("Sara", 7.2, 8.5, 6)
# print(f'A média do aluno é: {estudante2.calcular_media()}')
# estudante2.verificar_aprovacao()
# estudante2.mostrar_dados()
# estudante2.atualizar_notas(10,9,5)


#Questão Reserva de Hotel

class quartohotel:
    def __init__(self, numero, tipo, ocupado):
        self.numero = int(numero)
        self.tipo = str(tipo)
        self.ocupado = bool(ocupado)

    def reservar(self):

    def liberar(self):

    def status(self):

quartohotel_1 = quartohotel