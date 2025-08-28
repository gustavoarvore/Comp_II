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


##Questão Reserva de Hotel

# class quartohotel:
#     def __init__(self, numero, tipo, ocupado=1):
#         self.numero = int(numero)
#         self.tipo = str(tipo)
#         self.ocupado = bool(ocupado)

#     def reservar(self):
#         if self.ocupado == 0:
#             print(f"Desculpe, mas o quarto de {self.tipo}, número {self.numero}, está Ocupado!")
#         else:
#             print(f"O quarto de {self.tipo}, número {self.numero}, está disponível")

#     def liberar(self):
#         if self.reservar() == 0:
#             print(f"O quarto de {self.tipo}, número {self.numero}, estará disponível em breve!")
#         else:
#             print(f'O quarto de {self.tipo}, número {self.numero}, já disponível!')

#     # def status(self):

# quartohotel_1 = quartohotel(45, "Solteiro", 0)
# quartohotel_2 = quartohotel(76, "Casal", 1)
# quartohotel_1.reservar()
# quartohotel_2.reservar()
# quartohotel_1.liberar()
# quartohotel_2.liberar()

#Gerenciador de Pedidos de Restaurante

# class pedido:
#     def __init__(self, cliente):
#         self.cliente = str(cliente)
#         self.itens = []
#         self.total = 0.00

#     def adicionar_item(self, item, preço):
#         self.itens.append(item)
#         self.total += preço

#     def remover_item(self, item, preço):
#         if item in self.itens:
#             self.itens.remove(item)
#             self.total -= preço

#     def resumo(self):
#         itens_str = ','.join(self.itens)
#         print(f'Cliente: {self.cliente}\n Lista de Itens: {self.itens}\n Valor Total: {self.total}')

# pedido1 = pedido("Gustavo")
# pedido1.adicionar_item("banana", 6.00)
# pedido1.adicionar_item("cebola", 2.35)
# print(pedido1.resumo())

# pedido1.remover_item('cebola',2.35)
# print(pedido1.resumo())

#Locação de Carro

class veiculo:
    def __init__(self, modelo:str, ano:int):
        self.modelo = modelo
        self.ano = ano
        self.disponivel = True
        self.km_rodado = 0.0

    def alugar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"O carro de modelo {self.modelo} está Alugado!")
        else:
            print(f"O carro de modelo {self.modelo} está Disponível!")

    def devolver(self, km:float):
        if not self.alugar:
            self.alugar = True
            self.km_rodado += km
            print(f"O carro do modelo {self.modelo} está com {km} Km rodados")
        else:
            None

    def realizar_manutencao(self):
        self.km_rodado = 0.0
        print(f"Manutenção do veículo {self.modelo} completa! Quilometragem atual: {self.km_rodado}")

    def verificar_status(self):
        status = "Disponível" if self.disponivel else "alugado"
        print(f'O veículo do modelo {self.modelo} e ano {self.ano} está {status} e sua quilometragem é {self.km_rodado}')

    def necessita_manutencao(self):
        if self.km_rodado >= 10000.0:
            return True
        else: 
            return False

veiculo1 = veiculo("Palio 207", 2010)
print(veiculo1.verificar_status())
veiculo1.alugar()
veiculo1.devolver(11000.0)
print(veiculo1.verificar_status())
print(veiculo1.necessita_manutencao())
veiculo1.realizar_manutencao()
print(veiculo1.verificar_status())


        