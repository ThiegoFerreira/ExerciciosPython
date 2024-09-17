#  Escreva um algoritmo que leia um valor inicial A e imprima a sequência de valores do cálculo do 
# Fatorial: A! e o seu resultado. Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120
from math import prod

valor=int(input("Digite um valor: "))
fatorial=[]

for i in range(valor,0,-1):
    fatorial.append(i)

string = ' X '.join(str(numero) for numero in fatorial)
resultado= prod(fatorial)
print(f"{string} = {resultado}")