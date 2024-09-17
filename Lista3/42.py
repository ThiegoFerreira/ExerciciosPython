# Faça um programa que leia um conjunto não determinado de valores, um de cada vez, e 
# escreva para cada um dos valores lidos, o quadrado, o cubo e a raiz quadrada. Finalize a entrada 
# de dados com um valor negativo ou zero.

numero=1
while numero >0:
    numero = float(input("Digite um número: "))
    if numero >0:
        quadrado=numero**2
        cubo = numero**3
        raiz = numero**(1/2)
        print(f"{numero:.2f} ao quadrado é {quadrado:.2f}, ao cubo é {cubo:.2f} e a raiz quadrada é {raiz:.2f}")
else:
    print("Fim!")