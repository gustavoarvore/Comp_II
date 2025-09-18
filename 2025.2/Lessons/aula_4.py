#Herança Múltipla

class tratamentotermico:
    # classe base I
    def __init__(self, temperatura:float):
        self.temperatura = temperatura
    
    def tratar(self):
        return f'\nExecutando tratamento térmico a {self.temperatura} graus Celsius'

class controlequalidade:
    # classe base II
    def __init__(self, metodo:str, frequencia:int):
        self.metodo = metodo
        self.frequencia = frequencia

    def controlar(self):
        return f'Controle de qualidade usando o método {self.metodo} foi executado {self.frequencia} vezes por dia.'

class processometalurgico(tratamentotermico, controlequalidade):
    def __init__(self, temperatura:float, metodo:str, frequencia:int):
        tratamentotermico.__init__(self, temperatura)
        controlequalidade.__init__(self, metodo, frequencia)

processo1 = processometalurgico(850, "Ultrassonografia", 3)
print(processo1.tratar())
print(processo1.controlar())

# --------------------------------------------------------------------------------

class numero:
    # classe que representa um numero float
    def __init__(self, num:float):
        self.__num = num

    def __add__(self, other):
        print(f'\nRetorna {self.__num} + {other.__num}')
        return self.__num + other.__num

num_1 = numero(4.5)
num_2 = numero(1.7)

print(num_1 + num_2)