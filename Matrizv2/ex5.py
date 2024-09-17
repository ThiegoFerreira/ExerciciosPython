matriz=[]
l = 4
c = 4
i = 0
maior=0
while i < l:
    try:
        linha = []
        j = 0
        while j < c:
            num = int(input(f"Digite um número"))
            linha.append(num)
            j+=1        
        matriz.append(linha)
        i+=1
        soma=sum(linha)
        if soma > maior:
            maior = soma        
    except:
        print("Entrada inválida. Tente novamente.")  

x=0
while x < len(matriz):
    print(matriz[x])
    x+=1
print()

if sum(matriz[0]) == maior:
    print("Linha: 0")
elif sum(matriz[1]) == maior:
    print("Linha: 1")
elif sum(matriz[2]) == maior:
    print("Linha: 2")
elif sum(matriz[3]) == maior:
    print("linha: 3")

print(f"Soma: ",maior)