# exercicio 1

def dividir(dividendo, divisor):
    try:
        resultado = dividendo / divisor
        return resultado
    except ZeroDivisionError:
        print('Erro: Não é possivel dividir por zero')
        return None

print(dividir(10, 2))
print(dividir(5, 0))
print(dividir(10, 2))

