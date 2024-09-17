#Matriz 4X4 com zeros

l=4
c=4
matriz=[]
i=0
while i < l: # preenche as linhas (var l)
    linha = []
    j=0
    while j < c:
        linha.append(0)## preenche a coluna
        j +=1
    matriz.append(linha)##adiciona a lista na matriz
    i+=1

x=0
while x < len(matriz):
    print (matriz[x])
    x+=1
