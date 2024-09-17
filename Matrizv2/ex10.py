matriz=[]
somatoria=[]
l = 3
c = 3
i = 0

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
    except:
        print("Entrada inválida. Tente novamente.")  

x=0
while x < l:
    soma=0
    y=0
    while y<c:
        soma+=matriz[y][x]
        y+=1
    somatoria.append(soma)
    x+=1

print(somatoria)