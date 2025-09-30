# Questão: Classe Abstrata Pessoa
from abc import ABC, abstractmethod

class Pessoa(ABC):
    @abstractmethod
    def __init__(self, nome: str, idade: int, endereco: str):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def set_endereco(self, novo_endereco):
        self.endereco = novo_endereco
        return f'Seu endereço atual é: {self.endereco}'

    def aniversario(self):
        self.idade += 1
        return f'A sua idade atual é: {self.idade}'

    @abstractmethod
    def get_id(self):
        pass

    def __eq__(self, other):
        if isinstance(other, Pessoa):
            return self.get_id() == other.get_id()
        return False

# Questão: Subclasse PessoaFísica
from abc import ABC, abstractmethod

