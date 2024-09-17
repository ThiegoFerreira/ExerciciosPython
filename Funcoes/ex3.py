def numero_de_digitos(n):
    numero=str(n)
    res=len(numero)
    print(f'O número de digitos do número {n} é {res}.')


x= int(input("Informe um número: "))
numero_de_digitos(x)