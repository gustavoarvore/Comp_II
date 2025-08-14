def verificar_par_ou_impar(numero):
    if numero % 2 == 0:
        return "é par"
    else:
        return "ta de sacanagem?"

numero = int(input("Digite o numero: "))
resultado = verificar_par_ou_impar(numero)

print("Resultado:", resultado)