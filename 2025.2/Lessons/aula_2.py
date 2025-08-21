#Aula 2 - Criando uma classe e instanciando um objeto
#Data: 21/08/2025

class navio:
    def __init__(self, nome, tamanho):
        self.nome = nome
        self.tamanho = tamanho

    def navegar(self):
       print(f'O navio {self.nome} está navegando e tem o tamanho de {self.tamanho} metros.')


navio1 = navio("Titanic", 200)
navio2 = navio("Bismarck", 250)
navio1.navegar()
navio2.navegar()



class navio:
    def __init__(self, identificador, carga_inicial, capacidade_maxima):
        self.identificador = identificador
        self.carga = carga_inicial
        self.capacidade_maxima = capacidade_maxima
    
    def carregar(self, carga):
        if self.carga + carga <= self.capacidade_maxima:
            self.carga += carga
        else:
            print(f'erro: capacidade maxima excedida! O navio {self.identificador} aguenta até {self.capacidade_maxima} toneladas.')

    def descarregar(self, carga):
        if self.carga >= carga:
            self.carga -= carga
        else:
            print(f'erro: o navio {self.identificador} não tem carga suficiente para descarregar {carga} toneladas.')

    def verificar_carga(self):
        return self.carga

navio1 = navio("Navio A", 100, 500)
navio1.carregar(200)
navio1.descarregar(50)
