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
            f'O livro {self.titulo} não eh tao longo assim'
    
livro1 = livro("1984", "Jorge Orwell", 380)
print(livro1.detalhes())

livro2 = livro("Don Quixote", "Miguel de Cervantes", 863)
print(livro2.eh_longo())


class ebook:
    def __init__(self, titulo, autor, num_paginas, formato):
        super().__init__(titulo, autor, num_paginas)
        self.formato = formato

    def detalhes_ebook(self):
        return f'O livro {self.titulo}, escrito por {self.autor}, contem {self.num_paginas} paginas. Seu formato é {self.formato}'

ebook1 = ebook("Python para iniciantes", "João Silva", 250, "PDF")
print(ebook1.detalhes_ebook())
print(ebook1.eh_longo())

