# 9. Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido.

numeros=[]
cont=0
while cont< 10:
    try:
        num= int(input("Digite um número: "))
        numeros.append(num)
        cont+=1
    except:
        print("Entrada inválida!")
print(f"O menor valor digitado foi {min(numeros)} e o maior valor digitado foi {max(numeros)}.")

