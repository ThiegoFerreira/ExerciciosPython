matriz=[]
matriz_transposta=[]

l=2
c=3
i=0
n=1

while i < l:
    linha=[]
    j=0
    while j<c:
        linha.append(n)
        n+=1
        j+=1
    matriz.append(linha)
    i+=1

a=0
while a<l:
    print(matriz[a])
    a+=1

l2=3
c2=2
x=0
while x < l2:
    linha2=[]
    y=0
    while y<c2:
        linha2.append(matriz[y][x])
        y+=1
    matriz_transposta.append(linha2)
    x+=1
print()
d=0
while d<l2:
    print(matriz_transposta[d])
    d+=1