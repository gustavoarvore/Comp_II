from abc import ABC, abstractmethod
# import numpy as np

# 1. Classe Abstrata Pessoa
class pessoa(ABC):
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def set_endereco(self, novo_endereco):
        self.endereco = novo_endereco

    def aniversario(self):
        self.idade += 1

    @abstractmethod
    def get_id(self):
        pass

    def __eq__(self, other):
        return self.get_id() == other.get_id()


# 2. Subclasse PessoaFisica
class pessoafisica(pessoa):
    def __init__(self, nome, idade, endereco, cpf, estado_civil):
        super().__init__(nome, idade, endereco)
        self.cpf = cpf
        self.estado_civil = estado_civil

    def set_estado_civil(self, novo_estado):
        self.estado_civil = novo_estado

    def get_id(self):
        return self.cpf

    def __lt__(self, other):
        return self.idade < other.idade


# 3. Subclasse Empregado
class empregado(pessoafisica):
    def __init__(self, nome, idade, endereco, cpf, estado_civil, salario):
        super().__init__(nome, idade, endereco, cpf, estado_civil)
        self.salario = salario

    def aumentar_salario(self, valor):
        self.salario += valor

    def total_anual(self):
        return self.salario * 12

    def __add__(self, other):
        return self.salario + other.salario


# Classe PessoaJuridica (já dada no enunciado)
class pessoajuridica(pessoa):
    def __init__(self, nome, idade, endereco, cnpj):
        super().__init__(nome, idade, endereco)
        self.cnpj = cnpj

    def get_id(self):
        return self.cnpj


# 4. Classe Empresa
class empresa(pessoajuridica):
    def __init__(self, nome, idade, endereco, cnpj):
        super().__init__(nome, idade, endereco, cnpj)
        self.empregados = []

    def contratar(self, empregado):
        if empregado not in self.empregados:
            self.empregados.append(empregado)

    def demitir(self, empregado):
        if empregado in self.empregados:
            self.empregados.remove(empregado)

    def __len__(self):
        return len(self.empregados)


empregado1 = empregado("Joao", 30, "Rua A", "123", "Solteiro", 3000)
empregado2 = empregado("Maria", 40, "Rua B", "456", "Casado", 4000)
empregado3 = empregado("Carlos", 28, "Rua C", "123", "Solteiro", 3200)  

print(empregado1 == empregado2)  
print(empregado1 == empregado3)  

print(empregado3 < empregado1)  
print(empregado2 < empregado1)  

total_salarios = empregado1 + empregado2
print("Soma dos salários:", total_salarios) 

empregado1.aumentar_salario(500)
print("Novo salário mensal:", empregado1.salario)  
print("Salário anual:", empregado1.total_anual())  

empresa1 = empresa("Empresa X", 10, "Av. Central", "00.000.000/0001-00")

print("Empregados na empresa:", len(empresa1)) 
empresa1.contratar(empregado1)
empresa1.contratar(empregado2)
empresa1.contratar(empregado1)  
print("Empregados na empresa:", len(empresa1)) 

empresa1.demitir(empregado3) 
empresa1.demitir(empregado2)
print("Empregados na empresa:", len(empresa1)) 

empresa1.contratar(empregado3)
print("Empregados na empresa:", len(empresa1)) 
