matriz= []
n=1

for lin in range(3):
    linha = []
    for col in range(3):
        linha.append(n)
        n+=1
    matriz.append(linha)

for linha in matriz:
    print(linha)

# l=3
# c=3
# matriz=[]
# i=0
# n=1

# while i < l:
#     linha = []
#     j=0
#     while j < c:
#         linha.append(n)
#         n+=1
#         j +=1
#     matriz.append(linha)
#     i+=1

# x=0
# while x < len(matriz):
#     print (matriz[x])
#     x+=1