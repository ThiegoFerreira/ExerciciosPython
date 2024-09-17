#  Escreva um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima sua
# média.

cont=0
numeros=0
while cont < 10:
    try:
        num=int(input("Digite um número inteiro e positivo: "))
        if num >0:
            numeros=numeros+num
            media=numeros/10
            cont+=1
    except:
        print("Entrada inválida")
print(f"A média dos números digitados é {media}")

# numeros=0
# divisor=0
# for i in range(10):
#     num=int(input("Digite um número inteiro e positivo: "))
#     if num >0:
#         numeros=numeros+num
#         divisor+=1    
#     else:
#         num=int(input("O número deve ser inteiro e positivo: "))
# media=numeros/divisor
# print(f"A média dos números digitados é {media}")