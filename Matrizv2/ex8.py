matrix=[
[12,11,16],
[17,13,14],
[15,24,26]
]

pares=[]
l=3
c=3
i=0

while i < l:
    j=0
    while j< c:
        aux2=0
        if matrix[i][j] %2 ==0:
            pares.append(matrix[i] [j])
        j+=1       
    i+=1

print(f"Lista de números pares é: {pares}")