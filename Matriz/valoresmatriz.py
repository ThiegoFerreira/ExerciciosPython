matriz = [
    [24,34,44],
    [33,29,60],
    [21,18,19],
]

# i=0
# while i < len(matriz):
#     print(matriz[i])
#     i+=1

# matriz [1][2]

# print()
# i=0
# while i < len(matriz):
#     print(matriz[i])
#     i+=1

i = 0
while i < len(matriz): # contador que percorre as linhas
    j = 0
    while j < len(matriz[i]): # j contador que percorre as colunas
        print(matriz[i][j]) # matriz posição [i][j]
        j += 1
    i += 1
