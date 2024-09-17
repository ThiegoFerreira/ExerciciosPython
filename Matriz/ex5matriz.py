matriz=[]
l=8
c=8
i=0
n=0
while True:
    try:
        while i<l:
            linha = []
            j = 0
            while j < c:
                linha.append(n)
                j+=1
                n+=1
            matriz.append(linha)
            i+=1

        x=0
        while x < len(matriz):
            print(matriz[x])
            x+=1
        lin=int(input("Informe a linha: "))
        col=int(input("Informe a coluna: "))

        matriz [lin] [col] = "X"
    except:
        print("Linha ou coluna inválida. Digite novamente.")
    
        
    
