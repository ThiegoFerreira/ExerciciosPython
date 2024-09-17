# Escreva um programa que leia 10 inteiros e imprima sua média.

cont=0
numeros=0
while cont < 10:
    try:
        num=int(input("Digite um número: "))
        numeros=numeros+num
        media=numeros/10
        cont+=1
    except:
        print("Entrada inválida.")
print(f"A média dos números digitados é {media}")

# divisor=0
# numeros=0
# for i in range(10):
  
#     num=int(input("Digite um número: "))
#     numeros=numeros+num
#     divisor+=1
    
# media=numeros/divisor
# print(f"A média dos números digitados é {media}")
   