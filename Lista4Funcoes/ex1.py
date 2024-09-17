from math import pow

def potencia(x,y):
    for i in range(1,y+1):
        pot= x ** i
        print(f"{x} ** {i} = {pot} ")

x = int(input("Digite a base: "))
y = int(input("Digite o expoente: "))
potencia(x,y)