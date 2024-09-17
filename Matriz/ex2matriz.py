matriz=[]
l = 4
c = 4
i = 0
lin=0

while i < l:
    linha = []
    j = 0
    col=0
    while j < c:
        try:
            num = (input(f"Lin - {lin} Col - {col}: "))
            linha.append(num)
            j+=1
            col+=1
        except:
            print("Entrada inválida. Tente novamente.")    
    matriz.append(linha)
    i+=1
    lin+=1  

x=0
while x < len(matriz):
    print(matriz[x])
    x+=1