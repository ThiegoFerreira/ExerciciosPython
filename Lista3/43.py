import random
numero= random.randint(1,100)
print(numero)
num=int(input("tente adivinhar o número de 1 a 100: "))
while num != numero:
    if num > numero:
        num= int(input("Errado. Você digitou um número maior! Tente de novo: "))
    elif num < numero:
        num= int(input("Errado. Você digitou um número menor! Tente de novo: "))
else:
    print(f"Parabéns, você digitou {num} e o número aleatório é {numero}.")
