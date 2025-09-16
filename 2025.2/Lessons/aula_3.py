class livro:
    def __init__(self, titulo, autor, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas

    def detalhes(self):
        return f'O livro {self.titulo}, escrito por {self.autor}, contem {self.num_paginas} paginas.'

    def eh_longo(self):
        if self.num_paginas > 500:
            return f"O livro {self.titulo} eh longo"
        else:
            return f'O livro {self.titulo} não eh tao longo assim'
    
livro1 = livro("1984", "Jorge Orwell", 380)
print(livro1.detalhes())

livro2 = livro("Don Quixote", "Miguel de Cervantes", 863)
print(livro2.eh_longo())


class ebook(livro):
    def __init__(self, titulo, autor, num_paginas, formato):
        super().__init__(titulo, autor, num_paginas)
        self.formato = formato

    def detalhes_ebook(self):
        return f'O livro {self.titulo}, escrito por {self.autor}, contem {self.num_paginas} paginas. Seu formato é {self.formato}'

ebook1 = ebook("Python para iniciantes", "João Silva", 250, "PDF")
print(ebook1.detalhes_ebook())
print(ebook1.eh_longo())

class audiobook(livro):
    def __init__(self, titulo, autor, num_paginas, duracao):
        super().__init__(titulo, autor, num_paginas)
        self.duracao = duracao
        
    def detalhes_audiobook(self):
        return f'O livro {self.titulo}, escrito por {self.autor}, com a duracao de {self.duracao} minutos contem {self.num_paginas}.'
        
    def tempo_estimado_leitura(self, velocidade=1.0):
        return self.duracao/velocidade
        
audiobook1 = audiobook("O Senhor dos Aneis", "J.R.R.", 1000, 1200)
print(audiobook1.detalhes_audiobook())
print(audiobook1.tempo_estimado_leitura(1.0))
print(audiobook1.tempo_estimado_leitura(1.5))
print(audiobook1.tempo_estimado_leitura(2.0))

# ---------------------------------------------------------------------------------------------

class animal:
    def emitir_som(self):
        pass
    
class cachorro(animal):
    def emitir_som(self):
        return "au au"
    
class gato(animal):
    def emitir_som(self):
        return "miau"
    
cachorro1 = cachorro()
print(cachorro1.emitir_som())

gato1 = gato()
print(gato1.emitir_som())

# # ---------------------------------------------------------------------------------------------

class forma:
    def calcular_area(self):
        pass
    
class retangulo(forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def calcular_area(self):
        return self.largura * self.altura

class circulo(forma):
    def __init__(self, raio):
        self.raio = raio
        
    def calcular_area(self):
        return 3.14*self.raio**2
    
retangulo1 = retangulo(2, 2)
print(retangulo1.calcular_area())

circulo1 = circulo(7)
print(circulo1.calcular_area())