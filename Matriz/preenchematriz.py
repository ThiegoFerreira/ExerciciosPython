matrix=[]

l = int(input("Digite a quantidade de linhas: "))
c = int(input("Digite a quantidade de colunas: "))

i = 0
while i < l:
    linha = []
    j = 0
    while j < c:
        num = int(input("Digite um número: "))
        linha.append(num)
        j+=1
    matrix.append(linha)
    i+=1
    
x=0
while x < len(matrix):
    print(matrix[x])
    x+=1