#  Escreva um programa que peça ao usuário para digitar 10 valores e some-os.

# cont=0
# numeros=0
# while cont < 10:
#     num=int(input("Digite um número: "))
#     numeros=numeros+num
#     cont+=1
# print(f"A soma dos números é {numeros}")

total=0
for i in range(10):
    num=int(input("Digite um valor: "))
    total=total+num
print(f"A soma dos números é {total}")