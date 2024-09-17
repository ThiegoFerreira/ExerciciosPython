lista=[]
cont=0
while cont <9:
    try:
        lista+=[int(input("Digite um número: "))]
        cont+=1
    except:
        print("Entrada inválida. Tente novamente.")
print(lista)
print()

l=3
c=3
matriz=[]
i=0
n=lista[0]

while i < l:
    linha = []
    j=0
    while j < c:
        linha.append(n)
        n+=1
        j +=1
    linha.reverse()
    matriz.append(linha)
    i+=1
    
matriz.reverse()
x=0
while x < len(matriz):
    print (matriz[x])
    x+=1