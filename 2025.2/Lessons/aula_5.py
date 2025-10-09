# Blocos Try, Except e Else

try:
    x = int(input("Digite um numero: "))
except ValueError:
    print("Erro: Entrada Inválida. Digite um número!")
else:
    print(f'O numero digitado foi {x}')
    
# Exceções: Adicionando o bloco finally

try:
    x = int(input("Digite um numero: "))
except ValueError:
    print("Erro: Entrada Inválida. Digite um número!")
else:
    print(f'O numero digitado foi {x}')
finally:
    print("Bloco finally: execução finalizada!")

# Função usando raise

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("O denominador não pode ser zero!")
    return a / b

try:
    print(dividir(10, 0))
except ZeroDivisionError as zde:
    print(f'Erro: {zde}')

# Múltiplos except

try:
    num = int(input("Digite um numero: "))
    resultado = 10 / num
    print(f'Resultado: {resultado}')
except ValueError:
    print('Erro: Digite um numero!')
except ZeroDivisionError:
    print('Erro: Digite um valor diferente de 0')

# Exemplo de Aplicação

def calcular_fluxo(area, velocidade):
    if area <= 0:
        raise ValueError('Erro: área deve ser diferente de 0')
    if velocidade < 0:
        raise ValueError('Erro: valocidade não pode ser negativa')
    return area * velocidade
try:
    area = float(input('Digite a área (m^2): '))
    velocidade = float(input('Digite a velocidade (m/s): '))
    fluxo = calcular_fluxo(area, velocidade) 
    print(f'O fluxo de água é: {fluxo:.2f}ms/s^2')
except ValueError as e:
    print(f'Erro: {e}')
finally:
    print('calculo finalizado!')

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

