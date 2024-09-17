def positivo_negativo(n):
    if n > 0:
        argumento = 'P'
    elif n <=0:
        argumento = 'N'
    return argumento

x = int(input("Digite um número: "))

res = positivo_negativo(x)
print(res)