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

class estudante:
    def __init__(self, nome, nota1, nota2, nota3):
        self.nome = nome
        self.nota1 = float(nota1)
        self.nota2 = float(nota2)
        self.nota3 = float(nota3)

    def calcular_media(self):
        return ((self.nota1 + self.nota2 + self.nota3) / 3)

    def verificar_aprovacao(self):
        if calcular_media() >= 7:
            print("Aprovado")
        else:
            print("Reprovado")
            
    def atualizar_notas(self):
        while True:
            break
    
    def mostrar_dados():
        return

estudante1 = estudante(input("Digite o nome: "))
print(f'A média do aluno é: {estudante1.calcular_media()}')
print(f'Situação do(a) aluno(a): {estudante1.verificar_aprovacao()}')
print(f'Atualização das notas: {estudante1.atualizar_notas()}')
print(f'Dados do Estudante \n Nome: {self.nome}, Notas: {self.nota1}, {self.nota2}, {self.nota3}, Média: {}')