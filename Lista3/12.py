# Crie um programa que leia um número inteiro positivo N e imprima todos os números naturais
# de 0 até N em ordem crescente.
contador=0
numero=0
while numero <= 0:
    numero=int(input("Digite um número: "))
    
    for i in range(0,numero+1,1):
        print(i)