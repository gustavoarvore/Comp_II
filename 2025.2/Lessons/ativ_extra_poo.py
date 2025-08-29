class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        print(f'bem-vindo, {self.nome}! Sua idade é {self.idade} anos.')

class estudante(pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso
    
    def apresentar(self):
        print(f'bem-vindo, {self.nome}! Sua idade é {self.idade} anos. Seu curso é {self.curso}.')

# Criação de instâncias
pessoa1 = pessoa("João", 20)    
estudante1 = estudante("Maria", 22, "Engenharia")
pessoa1.apresentar()
estudante1.apresentar()