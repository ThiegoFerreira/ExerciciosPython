matriz=[]
nova_matriz=[]
l = 3
c = 3
i = 0

while i < l:
    try:
        linha = []
        linha2=[]
        j = 0
        while j < c:
            num = int(input(f"Digite um número"))
            linha.append(num)
            linha2.append(num*5)
            j+=1        
        matriz.append(linha)
        nova_matriz.append(linha2)
        i+=1
    except:
        print("Entrada inválida. Tente novamente.")  

x=0
while x < len(matriz):
    print(matriz[x])
    x+=1
print()
x=0
while x < len(nova_matriz):
    print(nova_matriz[x])
    x+=1

